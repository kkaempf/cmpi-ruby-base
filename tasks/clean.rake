task :clean do
  `rm -rf *~`
  `rm -rf */*~`
  `rm -rf */*/*~`
  `rm -f package/*.bz2`
  `rm -f Gemfile.lock`
  `rm -rf doc`
  `rm -rf .yardoc`
  `rm -rf pkg`
end
