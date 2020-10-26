import unittest
import re
import sys
import os
import json
import filecmp

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "parser"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "solver"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "adapter/visualiser_adapter"))
import Parser_Functions, Animation_parser, Domain_parser, Plan_generator, Initialise, Solver
from Problem_parser import *
from Predicates_generator import *

import Solver, Initialise
import Transfer

class TestOutputCost(unittest.TestCase):

    def test_output(self):
        url_link = ''
        animation_content = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'domain_ap.pddl'), 'r', encoding='utf-8-sig').read()
        domain_content = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'cost_domain.pddl'), 'r', encoding='utf-8-sig').read().lower()
        problem_content = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'cost_problem.pddl'), 'r', encoding='utf-8-sig').read().lower()

        plan = Plan_generator.get_plan(domain_content, problem_content, url_link)

        with open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + "plan_with_num_cost.json"), "w") as f:
            json.dump(plan, f)

if __name__ == '__main__':
    unittest.main()