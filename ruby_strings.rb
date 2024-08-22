require 'json'

require 'ruby_parser'

path = ARGV[0]

source = File.read(path)

# Source: https://stackoverflow.com/a/8439268
result = RubyParser.new.parse(source)
if result.nil? then
  result = []
end
result = result.flatten.to_a.select {|elt| elt.is_a?(String)}

File.open(path + '.json', 'w') do |f|
  f.write(result.to_json)
end
