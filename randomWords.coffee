#
#    Random words to generate passphrase using dice
#

fs = require 'stream'

class randomWords

  constructor: ->
    @stream = fs.CreateReadableStream '/usr/share/dict'


