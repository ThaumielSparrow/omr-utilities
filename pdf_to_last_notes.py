import music21

score = music21.converter.parse('moonlight-a4.mxl')

notes = []
for part in score.parts:
    for note_or_chord in part.flat.notesAndRests:
        if isinstance(note_or_chord, music21.note.Note) or isinstance(note_or_chord, music21.chord.Chord):
            notes.append(note_or_chord)

last_notes = notes[-10:]

for note_or_chord in last_notes:
    if isinstance(note_or_chord, music21.note.Note):
        print(note_or_chord.pitch)
    elif isinstance(note_or_chord, music21.chord.Chord):
        print(note_or_chord.pitches)