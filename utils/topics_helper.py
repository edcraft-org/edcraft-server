from question.sort.utils import SORT_TOPIC_SUBTOPIC_MAPPING
from question.tree.utils import TREE_TOPIC_SUBTOPIC_MAPPING

# Combine the mappings
TOPIC_SUBTOPIC_MAPPING = {
    **SORT_TOPIC_SUBTOPIC_MAPPING,  # Merge the sort mappings
    **TREE_TOPIC_SUBTOPIC_MAPPING,  # Merge the tree mappings
    # Add more topics here
}

def get_question_class(topic, subtopic):
    try:
        return TOPIC_SUBTOPIC_MAPPING[topic][subtopic]
    except KeyError:
        raise ValueError(f"Invalid topic '{topic}' or subtopic '{subtopic}'")

def get_topics():
    return list(TOPIC_SUBTOPIC_MAPPING.keys())

def get_subtopics(topic):
    try:
        return list(TOPIC_SUBTOPIC_MAPPING[topic].keys())
    except KeyError:
        raise ValueError(f"Invalid topic '{topic}'")
