import logging
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer)

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    dialog_training_data_file = './data/stories2.md'
    path_to_model = './models/dialogue'
    featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(),
                                            max_history=5)
    domain_file = 'domain.yml'
    agent = Agent(domain_file,
                policies=[MemoizationPolicy(max_history=5),
                            KerasPolicy(featurizer)])
    training_data = agent.load_data(dialog_training_data_file)
    agent.train(training_data,
        augmentation_factor=50,
        validation_split=0.2)
agent.persist(path_to_model)