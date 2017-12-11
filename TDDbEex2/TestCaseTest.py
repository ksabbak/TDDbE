from TestCase import TestCase
from WasRun import WasRun
from TestResult import TestResult
from TestSuite import TestSuite

class TestCaseTest(TestCase):
	def setUp(self):
		self.result = TestResult()

	def testTemplateMethod(self):
		test= WasRun("testMethod")
		test.run(self.result)
		assert test.log == "setUp testMethod tearDown "

	def testResult(self):
		test = WasRun("testMethod")
		test.run(self.result)
		assert result.summary() == "1 run, 0 failed"

	def testFailedResultFormatting(self):
		result = TestResult()
		result.testStarted()
		result.testFailed()
		assert result.summary() == "1 run, 1 failed"

	def testFailedResult(self):
		test = WasRun("testBrokenMethod")
		test.run(self.result)
		assert result.summary() == "1 run, 1 failed"

	def testTestSuite(self):
		suite = TestSuite()
		suite.add(WasRun("testMethod"))
		suite.add(WasRun("testBrokenMethod"))
		result = TestResult()
		suite.run(result)
		print "???"
		assert result.summary() == "2 run, 1 failed" 

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testTestSuite"))
result = TestResult()
suite.run(result)
print result.summary()

