notes = {'0' : ['s', 'r2', 'g2', 'p', 'd2'], '1' : ['s', 'r2', 'g2', 'm1', 'p', 'd2', 'n2'], '2' : ['s', 'r2', 'g2', 'p', 'd2', 'n2']}
mapping = {'s' : 'c'
           	,'r1' : 'c#'
           	,'r2' : 'd'
           	,'g1' : 'd#'
           	,'g2' : 'e'
           	,'m1' : 'f'
           	,'m2' : 'f#'
           	,'p' : 'g'
           	,'d1' : 'g#'
           	,'d2' : 'a'
           	,'n1' : 'a#'
           	,'n2' : 'b'}
def Translate(note, octave=4):
  if len(note) == 2 and note[1] == ".":
    octave = octave - 1
  if note.isupper():
    note = note.lower()
    octave += 1
  
  try:
    print "This is the note " + note[0:]
    return mapping[note[0:]] + str(octave)
  except KeyError:
    print "The note %s cannot be mapped."%(note[0:])
    return


def Base_Note():
    return mapping['s']