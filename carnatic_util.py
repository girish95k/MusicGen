import util

def ConvertString(s):
  """
      g , g, r , , , 
      [(g, 8), (g, 8), (r, 16)]
      (assuming tempo = 4) 
  """

  return ConvertLengthToTempo(CollectNotes(s))

def CollectNotes(s):
  """
        g , g, r , , ,  
        [(g, 2) (g, 2) (r, 4)]
  """

  standard_length = 1

  li = s.split()
  notes = []
  previous_note = ''
  previous_length = 0

  for c in li:
    if c != ',':
      notes.append((c, standard_length))
    if c == ',':
      try:
        (previous_note, previous_length) = notes[-1]
      except IndexError:
        print "Error"
        return
      notes[-1] = (previous_note, previous_length+standard_length)
  return notes

def ConvertLengthToTempo(notes):
  # find the lcm of all the lengths
  note_lengths = [b for (a, b) in notes]
  lcm = util.lcm_many(*note_lengths)

  tempo_notes = []
  for (a, b) in notes:
    tempo_notes.append((a, lcm/b))

  return tempo_notes



def PreProcessScore(s):
  s = s.replace("|", " ")
  s = s.replace("  ", " ")
  return s

def ReadFromFile(f):  
  s = f.read()
  s = PreProcessScore(s)
  l = ConvertString(s)
  return l

