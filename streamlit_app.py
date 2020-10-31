import os
import pkg_resources, imp

import spacy_streamlit

models = ["ja_core_news_lg", "ja_core_news_md", "ja_core_news_sm"]
#models = ["ja_core_news_sm"]

# 未ダウンロードのモデルファイルがある場合はダウンロード
for model in models:
    try:
        imp.find_module(model)
    except ImportError:
        os.system("python -m spacy download {}".format(model))
        imp.reload(pkg_resources)

spacy_streamlit.visualize(models, "")

