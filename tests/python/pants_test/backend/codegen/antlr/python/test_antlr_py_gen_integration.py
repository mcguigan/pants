# Copyright 2016 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.testutil.interpreter_selection_utils import skip_unless_python27_present
from pants.testutil.pants_run_integration_test import PantsRunIntegrationTest


class AntlrPyGenIntegrationTest(PantsRunIntegrationTest):

  @skip_unless_python27_present
  def test_antlr_py_gen_integration(self):
    result = self.run_pants(['run', '--args="123 * 321"', 'testprojects/src/python/antlr:eval-bin'])
    self.assertEqual(0, result.returncode)
    self.assertIn('39483', result.stdout_data)

  @skip_unless_python27_present
  def test_python_invalid_antlr_grammar_fails(self):
    result = self.run_pants(['gen',
                             'testprojects/src/antlr/python/test:antlr_failure'])
    self.assertNotEqual(0, result.returncode)
    self.assertIn('grammar file testprojects/src/antlr/python/test/bogus.g has no rules',
                  result.stdout_data)
