require 'rake/testtask'

VERSION  = '0.0.1'
TOPLEVEL = File.dirname(__FILE__)
NAME     = File.basename TOPLEVEL
MOFDIR   = "/usr/share/mof/#{NAME}"
CMPIDIR  = "/usr/share/cmpi"
DESTDIR ||= ""

task :default => [:test]

Dir['tasks/**/*.rake'].each { |t| load t }
