from ...abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class MSMARCO(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            "name": "MSMARCO",
            "beir_name": "msmarco",
            "description": "MS MARCO is a collection of datasets focused on deep learning in search",
            "reference": "https://microsoft.github.io/msmarco/",
            "type": "Retrieval",
            "category": "s2p",
            "eval_splits": ["dev", "test"],  # "validation" if using latest BEIR i.e. HFDataLoader
            "eval_langs": ["en"],
            "main_score": "ndcg_at_10",
        }
