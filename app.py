import os, glob, re, streamlit as st, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Hybrid RAG Chatbot", page_icon="💬", layout="wide")
st.title("Hybrid RAG Chatbot — Local Knowledge Base")

st.caption("Ask a question. The app retrieves relevant passages from local markdown files using TF‑IDF (embeddings optional).")

# Optional embeddings (if user installs sentence-transformers)
use_st = False
model = None
try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    use_st = True
except Exception:
    use_st = False

def load_kb(folder="data/knowledge_base"):
    chunks = []
    for path in glob.glob(os.path.join(folder, "*.md")):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        # naive chunking by headings or paragraphs
        parts = re.split(r"\n\s*\n", text)
        for p in parts:
            p = p.strip()
            if len(p) > 20:
                chunks.append(p)
    return chunks

chunks = load_kb()
st.write(f"Knowledge chunks loaded: {len(chunks)}")

query = st.text_input("Your question:", placeholder="e.g., How is data secured?")
top_k = st.slider("Results", 1, 5, 3)

if st.button("Search") and query:
    if use_st:
        q_emb = model.encode([query])
        c_emb = model.encode(chunks)
        sims = (q_emb @ c_emb.T)[0]
    else:
        tfidf = TfidfVectorizer(stop_words="english")
        X = tfidf.fit_transform(chunks + [query])
        sims = cosine_similarity(X[-1], X[:-1])[0]

    idxs = np.argsort(-sims)[:top_k]
    for rank, i in enumerate(idxs, start=1):
        st.markdown(f"**{rank}. (score={sims[i]:.3f})**")
        st.write(chunks[i])
        st.markdown("---")

st.markdown("**How it works**: Local retrieval only. To answer with an LLM, feed top chunks into a model API (e.g., OpenAI) — not included in this template.")
