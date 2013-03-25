#
# Testcase for proper registration of all classes
#
require 'rubygems'
require 'sfcc'
require 'test/unit'
require 'provider-testing'

class Test_Registration < Test::Unit::TestCase
  def setup
    @client, @op = ProviderTesting.setup '', 'test/test'
  end

  def teardown
    ProviderTesting.teardown
  end

  def test_registered
    # all these class names must appear once in enumerate class names
    classes = [ "RCP_ComputerSystem.mof",
      "RCP_OperatingSystem.mof",
      "RCP_OSProcess.mof",
      "RCP_PhysicalMemory.mof",
      "RCP_Processor.mof",
      "RCP_RunningOS.mof",
      "RCP_UnixProcess.mof"
    ]
    
    @client.class_names(@op).each do |name|
      assert classes.delete(name)
    end
    assert_equal [], classes
  end

end
