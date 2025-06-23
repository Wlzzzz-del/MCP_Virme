graph [
  node [
    id "Host ABC1_2"
    label "Host ABC1_2"
    x 100
    y 100
  ]
  node [
    id "s1"
    label "s1"
    x 200
    y 200
  ]
  node [
    id "switch s1_b2"
    label "switch s1_b2"
    x 150
    y 150
  ]
  node [
    id "host1"
    label "host1"
    x 250
    y 150
  ]
  node [
    id "219.41.0.9"
    label "219.41.0.9"
    x 300
    y 300
  ]
  node [
    id "74.0.0.6"
    label "74.0.0.6"
    x 400
    y 400
  ]
  node [
    id "s_9"
    label "s_9"
    x 500
    y 500
  ]
  node [
    id "h1"
    label "h1"
    x 600
    y 600
  ]
  node [
    id "s37"
    label "s37"
    x 700
    y 700
  ]
  node [
    id "Host 19"
    label "Host 19"
    x 800
    y 800
  ]
  node [
    id "AB:cd:12:e3:f4:5e"
    label "AB:cd:12:e3:f4:5e"
    x 900
    y 900
  ]
  node [
    id "host 37"
    label "host 37"
    x 1000
    y 1000
  ]
  node [
    id "core switch"
    label "core switch"
    x 1100
    y 1100
  ]
  node [
    id "h49"
    label "h49"
    x 1200
    y 1200
  ]
  node [
    id "A01b2c3d4e5f"
    label "A01b2c3d4e5f"
    x 1300
    y 1300
  ]
  edge [
    source "Host ABC1_2"
    target "s1"
    color "blue"
    bw "1Gbps"
  ]
  edge [
    source "switch s1_b2"
    target "host1"
    color "red"
    bw "NA"
  ]
  edge [
    source "219.41.0.9"
    target "s1"
    color "yellow"
    bw "NA"
  ]
  edge [
    source "74.0.0.6"
    target "s1"
    color "green"
    bw "0.5 MBps"
  ]
  edge [
    source "s1"
    target "s_9"
    color "purple"
    bw "NA"
  ]
  edge [
    source "h1"
    target "74.0.0.6"
    color "orange"
    bw "NA"
  ]
  edge [
    source "s37"
    target "Host 19"
    color "pink"
    bw "NA"
  ]
  edge [
    source "Host 19"
    target "AB:cd:12:e3:f4:5e"
    color "black"
    bw "2.1 mbps"
  ]
  edge [
    source "host 37"
    target "74.0.0.6"
    color "brown"
    bw "0.5 MBps"
  ]
  edge [
    source "core switch"
    target "h49"
    color "cyan"
    bw "0.5 MBps"
  ]
  edge [
    source "switch s1_b2"
    target "A01b2c3d4e5f"
    color "gray"
    bw "NA"
  ]
  edge [
    source "219.41.0.9"
    target "Host ABC1_2"
    color "magenta"
    bw "0.5 MBps"
  ]
  edge [
    source "74.0.0.6"
    target "A01b2c3d4e5f"
    color "lime"
    bw "NA"
  ]
  edge [
    source "h1"
    target "host 37"
    color "teal"
    bw "NA"
  ]
  edge [
    source "Host ABC1_2"
    target "h49"
    color "olive"
    bw "NA"
  ]
  edge [
    source "host1"
    target "Host ABC1_2"
    color "navy"
    bw "NA"
  ]
]
