# Welcome to Sonic Pi v3.0.1

live_loop :listen do
  use_real_time
  note = sync "/osc/play_this"
  play note[0]
end
