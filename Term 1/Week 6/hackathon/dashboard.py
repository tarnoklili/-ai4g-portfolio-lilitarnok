"""Dashboard: how the mood about AI coding tools changes over time.

Run (in the folder that has config.py and data/items.csv):
    pip install streamlit pandas plotly
    streamlit run dashboard.py

To see new data: `git pull` (the collector commits to GitHub), then press
"Reload data" in the sidebar.
"""
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import config

TZ = "Europe/Amsterdam"
DATA = Path(__file__).parent / "data" / "items.csv"
LABELS = ["negative", "neutral", "positive"]
GOAL_ITEMS, GOAL_HOURS = 300, 48

# Palette: blue <-> red poles with a gray neutral (diverging, ordered sentiment).
PAL = {
    "light": dict(surface="#fcfcfb", ink="#0b0b0b", ink2="#52514e", muted="#898781",
                  grid="#e1e0d9", axis="#c3c2b7", negative="#e34948", neutral="#c3c2b7",
                  positive="#2a78d6", line="#2a78d6"),
    "dark": dict(surface="#1a1a19", ink="#f0efec", ink2="#c3c2b7", muted="#898781",
                 grid="#2c2c2a", axis="#383835", negative="#e66767", neutral="#5b5a56",
                 positive="#3987e5", line="#3987e5"),
}

st.set_page_config(page_title="AI Coding Pulse", layout="wide")

try:
    _v = tuple(int(x) for x in st.__version__.split(".")[:2])
except Exception:
    _v = (1, 0)
# Newer Streamlit uses width="stretch"; older versions use use_container_width.
STRETCH = {"width": "stretch"} if _v >= (1, 50) else {"use_container_width": True}


def theme_name():
    try:
        return "dark" if st.context.theme.type == "dark" else "light"
    except Exception:
        return "light"


@st.cache_data(ttl=60, show_spinner=False)
def load(path, mtime):
    df = pd.read_csv(path)
    df["created_at"] = pd.to_datetime(df["created_at"], utc=True, errors="coerce")
    df["collected_at"] = pd.to_datetime(df["collected_at"], utc=True, errors="coerce")
    df = df.dropna(subset=["created_at"]).copy()
    df["label"] = df["label"].astype(str).str.lower()
    df = df[df["label"].isin(LABELS)].drop_duplicates("item_id")
    df["local"] = df["created_at"].dt.tz_convert(TZ)
    return df.sort_values("created_at").reset_index(drop=True)


def is_core(text):
    """Stricter relevance: names an AI coding tool (the 'wide' rule also lets in
    comments that merely mention AI together with programming)."""
    t = str(text)
    return bool(config.TOOLS_RE.search(t) or (config.CURSOR_RE.search(t) and config.AI_CONTEXT_RE.search(t)))


def style(fig, c, height, ytitle=None, yrange=None):
    fig.update_layout(
        height=height, margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=c["ink2"], family="system-ui, -apple-system, 'Segoe UI', sans-serif", size=13),
        legend=dict(orientation="h", y=1.12, x=0, font=dict(color=c["ink2"])),
        hovermode="x unified",
    )
    fig.update_xaxes(showgrid=False, linecolor=c["axis"], tickfont=dict(color=c["muted"]))
    fig.update_yaxes(gridcolor=c["grid"], gridwidth=1, zeroline=False, linecolor=c["axis"],
                     tickfont=dict(color=c["muted"]), title=ytitle, range=yrange)
    return fig


c = PAL[theme_name()]

st.title("AI Coding Pulse")
st.caption("Mood of Hacker News comments about AI coding tools (Copilot, Cursor, Claude Code and similar). "
           "For an engineering team lead deciding whether to roll these tools out.")

if not DATA.exists():
    st.error(f"No data yet: {DATA} does not exist. Run `git pull`, or run the collector first.")
    st.stop()

df_all = load(str(DATA), DATA.stat().st_mtime)
if df_all.empty:
    st.warning("The data file has no usable rows yet.")
    st.stop()

# ---- filters: one row of controls scopes everything below -------------------
with st.sidebar:
    st.header("Filters")
    step = st.radio("Time step", ["Hour", "Day"], horizontal=True, key="step")
    relevance = st.radio("Which comments", ["Wide (everything collected)", "Core (names an AI coding tool)"], key="relevance")
    min_n = st.slider("Warn when a time step has fewer items than", 1, 20, 5)
    dmin, dmax = df_all["local"].dt.date.min(), df_all["local"].dt.date.max()
    rng = st.date_input("Dates", (dmin, dmax), min_value=dmin, max_value=dmax)
    start, end = (rng[0], rng[-1]) if isinstance(rng, (tuple, list)) and len(rng) else (rng, rng)
    if st.button("Reload data"):
        st.cache_data.clear()
        st.rerun()

df = df_all[(df_all["local"].dt.date >= start) & (df_all["local"].dt.date <= end)]
if relevance.startswith("Core"):
    df = df[df["text"].map(is_core)]
if df.empty:
    st.warning("No items match these filters.")
    st.stop()

# ---- progress against the assignment goal ----------------------------------
running_h = (df_all["collected_at"].max() - df_all["collected_at"].min()).total_seconds() / 3600
p1, p2 = st.columns(2)
p1.progress(min(len(df_all) / GOAL_ITEMS, 1.0), text=f"Items collected: {len(df_all)} of {GOAL_ITEMS}")
p2.progress(min(running_h / GOAL_HOURS, 1.0), text=f"Hours of collection: {running_h:.0f} of {GOAL_HOURS}")

# ---- headline numbers -------------------------------------------------------
n_total = len(df)
share = df["label"].value_counts(normalize=True).reindex(LABELS, fill_value=0)
overall = share["positive"] - share["negative"]
first_run = df_all["collected_at"].min()
live = int((df["created_at"] >= first_run).sum())
k1, k2, k3, k4 = st.columns(4)
k1.metric("Comments shown", f"{n_total}")
k2.metric("Overall mood", f"{overall:+.2f}", help="Share positive minus share negative. -1 is all negative, +1 all positive.")
k3.metric("Negative / neutral / positive", f"{share['negative']:.0%} / {share['neutral']:.0%} / {share['positive']:.0%}")
k4.metric("Posted after the first run", f"{live}")

# ---- aggregate per time step ------------------------------------------------
freq = "h" if step == "Hour" else "D"
d = df.copy()
d["bucket"] = d["local"].dt.floor(freq)
g = d.groupby(["bucket", "label"]).size().unstack(fill_value=0).reindex(columns=LABELS, fill_value=0)
full = pd.date_range(g.index.min(), g.index.max(), freq=freq, tz=TZ)
g = g.reindex(full, fill_value=0)
g["n"] = g[LABELS].sum(axis=1)
g["mood"] = (g["positive"] - g["negative"]) / g["n"].where(g["n"] > 0)

# ---- chart 1: mood over time ------------------------------------------------
st.subheader(f"Mood per {step.lower()}")
enough = g[g["n"] >= min_n]
few = g[(g["n"] > 0) & (g["n"] < min_n)]
cd = lambda x: x[["n", "negative", "neutral", "positive"]].to_numpy()  # noqa: E731
hover = ("Mood %{y:+.2f}<br>%{customdata[0]} items "
         "(%{customdata[1]} negative, %{customdata[2]} neutral, %{customdata[3]} positive)<extra></extra>")
fig = go.Figure()
fig.add_hline(y=0, line_color=c["axis"], line_width=1)
fig.add_trace(go.Scatter(x=g.index, y=g["mood"], mode="lines", line=dict(color=c["line"], width=2),
                         connectgaps=False, hoverinfo="skip", showlegend=False))
fig.add_trace(go.Scatter(x=enough.index, y=enough["mood"], mode="markers", name=f"Mood ({min_n}+ items)",
                         marker=dict(color=c["line"], size=9, line=dict(color=c["surface"], width=2)),
                         customdata=cd(enough), hovertemplate=hover))
if len(few):
    fig.add_trace(go.Scatter(x=few.index, y=few["mood"], mode="markers", name=f"Few items (under {min_n}): unreliable",
                             marker=dict(color=c["surface"], size=9, line=dict(color=c["muted"], width=2)),
                             customdata=cd(few), hovertemplate=hover))
style(fig, c, 300, "Mood (-1 negative, +1 positive)", [-1, 1])
st.plotly_chart(fig, **STRETCH)

# ---- chart 2: how many items, split by sentiment ---------------------------
st.subheader(f"Items per {step.lower()}, by sentiment")
fig2 = go.Figure()
for lab in LABELS:
    fig2.add_trace(go.Bar(x=g.index, y=g[lab], name=lab.capitalize(), marker_color=c[lab],
                          marker_line_color=c["surface"], marker_line_width=2))
fig2.update_layout(barmode="stack", bargap=0.25)
style(fig2, c, 280, "Number of comments")
st.plotly_chart(fig2, **STRETCH)

# ---- open the comments behind a peak or dip --------------------------------
st.subheader("Open the comments behind a peak or dip")
valid = g[g["n"] >= min_n] if (g["n"] >= min_n).any() else g[g["n"] > 0]
labels_for = {ts: f"{ts:%a %d %b %H:%M} | mood {r['mood']:+.2f} | {int(r['n'])} items" for ts, r in valid.iterrows()}
mode = st.radio("Show me", ["Most positive", "Most negative", "Busiest", "Pick myself"], horizontal=True, key="mode")
if mode == "Most positive":
    chosen = valid["mood"].idxmax()
elif mode == "Most negative":
    chosen = valid["mood"].idxmin()
elif mode == "Busiest":
    chosen = valid["n"].idxmax()
else:
    chosen = st.selectbox("Time step", list(labels_for), format_func=labels_for.get)
st.write(f"**{labels_for[chosen]}**")
delta = pd.Timedelta(hours=1) if step == "Hour" else pd.Timedelta(days=1)
rows = d[(d["bucket"] == chosen)].sort_values("local")
st.dataframe(
    rows.assign(time=rows["local"].dt.strftime("%a %d %b %H:%M"))[["time", "label", "score", "text"]],
    **STRETCH, hide_index=True,
    column_config={"text": st.column_config.TextColumn("Comment", width="large"),
                   "label": "Model says", "score": st.column_config.NumberColumn("Confidence", format="%.2f")},
)

# ---- table twin + limits ----------------------------------------------------
with st.expander("Show the numbers as a table"):
    t = g.copy()
    t.index = t.index.strftime("%a %d %b %H:%M")
    st.dataframe(t.rename(columns={"n": "items", "mood": "mood score"}), **STRETCH)

st.info(
    "**Read with care.** Hacker News commenters are mostly developers, so this shows what developers say, "
    "not managers, students or people who do not post. The model was trained on tweets and misreads "
    "sarcasm, jargon and mixed messages. Small numbers of items make the mood jump around: look at the "
    "item counts, not only the line. Do not use this as the only basis for a decision."
)
