import unittest
import re
import sys
import os
import json
import filecmp

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "parser"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "solver"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../vfg/' + "adapter/visualiser_adapter"))
import Parser_Functions, Animation_parser, Domain_parser, Plan_generator
from Problem_parser import *
from Predicates_generator import *

import Solver, Initialise
import Transfer

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        #print(Parser_Functions.parse_objects('test'))
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_visitall(self):
        url_link = ''
        animation_content = open('domain_ap.pddl', 'r', encoding='utf-8-sig').read()
        domain_content = open('domain.pddl', 'r', encoding='utf-8-sig').read().lower()
        problem_content = open('problem12.pddl', 'r', encoding='utf-8-sig').read().lower()

        plan = Plan_generator.get_plan(domain_content, problem_content, url_link)

        predicates_list = Domain_parser.get_domain_json(domain_content)
        problem_dic = get_problem_dic(problem_content, predicates_list)
        object_list = get_object_list(problem_content)

        animation_profile = json.loads(Animation_parser.get_animation_profile(animation_content, object_list))

        stages = get_stages(plan, problem_dic, problem_content, predicates_list)

        result = Solver.get_visualisation_dic(stages, animation_profile, plan['result']['plan'], problem_dic)
        objects_dic = Initialise.initialise_objects(stages["objects"], animation_profile)
        final = Transfer.generate_visualisation_file(result, list(objects_dic.keys()), animation_profile, plan['result']['plan'])

        with open("test.vfg", "w") as f:
            json.dump(final, f)
        
        output_content = open("test.vfg", 'r', encoding='utf-8-sig').read()

        expected_content = open("expect_output.vfg", 'r', encoding='utf-8-sig').read()
        #print(output_content, expected_content)

        self.assertTrue(filecmp.cmp('test.vfg', 'expect_output.vfg', shallow=False))

if __name__ == '__main__':
    unittest.main()