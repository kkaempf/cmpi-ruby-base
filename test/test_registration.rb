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
    classes = [ "RCP_ComputerSystem",
      "RCP_OperatingSystem",
      "RCP_OSProcess",
      "RCP_PhysicalMemory",
      "RCP_Processor",
      "RCP_RunningOS",
      "RCP_UnixProcess"
    ]
    
    @client.class_names(@op, Sfcc::Flags::DeepInheritance).each do |name|
      classes.delete(name.to_s)
    end
    assert_equal [], classes
  end

end
