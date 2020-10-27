import unittest
import re
import sys
import os
import json
import filecmp

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "parser"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "solver"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "adapter/visualiser_adapter"))
import Parser_Functions, Animation_parser, Domain_parser, Plan_generator, Initialise, Solver, Predicates_generator
from Problem_parser import *
from Predicates_generator import *

import Solver, Initialise
import Transfer
#
# class TestOutputCost(unittest.TestCase):
#
#     def test_output(self):
#         url_link = ''
#         animation_content = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'domain_ap.pddl'), 'r', encoding='utf-8-sig').read()
#         domain_content = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'cost_domain.pddl'), 'r', encoding='utf-8-sig').read().lower()
#         problem_content = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'cost_problem.pddl'), 'r', encoding='utf-8-sig').read().lower()
#
#         plan = Plan_generator.get_plan(domain_content, problem_content, url_link)
#
#         with open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + "plan_with_num_cost.json"), "w") as f:
#             json.dump(plan, f)
#
# if __name__ == '__main__':
#     unittest.main()

# import json
# from server.app.vfg.adapter.visualiser_adapter import Transfer
# from server.app.vfg.parser import Parser_Functions, Plan_generator, Domain_parser, Problem_parser, Animation_parser, \
#     Predicates_generator
# from server.app.vfg.solver import Initialise, Solver


def test():
    # domain_file = open("domain2.pddl", 'r', encoding='utf-8-sig').read()
    # problem_file = open("problem2.pddl", 'r', encoding='utf-8-sig').read()
    # animation_file = open("domain_ap2.pddl", 'r', encoding='utf-8-sig').read()
    domain_file = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'cost_domain.pddl'), 'r',
                       encoding='utf-8-sig').read()
    problem_file = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'cost_problem.pddl'), 'r',
                        encoding='utf-8-sig').read().lower()
    animation_file = open(os.path.abspath(os.path.dirname(__file__) + '/../unit_test/' + 'domain_ap.pddl'), 'r',
                          encoding='utf-8-sig').read().lower()
    domain_file = Parser_Functions.comment_filter(domain_file)
    problem_file = Parser_Functions.comment_filter(problem_file)
    animation_file = Parser_Functions.comment_filter(animation_file)
    url_link = "http://solver.planning.domains/solve"
    plan = Plan_generator.get_plan(domain_file, problem_file, url_link)
    predicates_list = Domain_parser.get_domain_json(domain_file)
    problem_dic = Problem_parser.get_problem_dic(problem_file, predicates_list)
    object_list = Problem_parser.get_object_list(problem_file)
    animation_profile = json.loads(Animation_parser.get_animation_profile(animation_file, object_list))
    stages = Predicates_generator.get_stages(plan, problem_dic, problem_file, predicates_list)
    objects_dic = Initialise.initialise_objects(stages["objects"], animation_profile)
    result = Solver.get_visualisation_dic(stages, animation_profile, plan['result']['plan'], problem_dic)
    visualisation_file = Transfer.generate_visualisation_file(result, list(objects_dic.keys()), animation_profile,
                                                              plan['result']['plan'])
    return visualisation_file

if __name__ == "__main__":
    test()