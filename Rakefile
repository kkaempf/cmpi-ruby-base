VERSION  = '0.0.1'
TOPLEVEL = File.dirname(__FILE__)
NAME     = File.basename TOPLEVEL
MOFDIR   = "/usr/share/mof/#{NAME}"
CMPIDIR  = "/usr/share/cmpi"
DESTDIR  = ENV['DESTDIR']

task :default => [:test]

IO.popen('gem contents provider-testing').each do |l|
  if l =~ %r{template/Rakefile}
    Dir[File.join(File.dirname(l), "tasks", "**", "*.rake")].each { |t| load t }
    break
  end
end

Dir['tasks/**/*.rake'].each { |t| load t }
