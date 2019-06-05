#~# ORIGINAL

[
  [<<~'},'] # comment
  },
]

#~# EXPECTED

[
  [<<~'},'], # comment
  },
]

#~# ORIGINAL

[
  [<<~'},'], # comment
  },
]

#~# EXPECTED

[
  [<<~'},'], # comment
  },
]

#~# ORIGINAL

[
  [<<~'},'], # comment
  },
  2,
]

#~# EXPECTED

[
  [<<~'},'], # comment
  },
  2,
]

#~# ORIGINAL

[
  [<<~EOF] # comment
  EOF
]

#~# EXPECTED

[
  [<<~EOF], # comment
  EOF
]

#~# ORIGINAL

begin
  foo = <<~STR
    some

    thing
  STR
end

#~# EXPECTED

begin
  foo = <<~STR
    some

    thing
  STR
end

#~# ORIGINAL

<<~EOF
  foo
   bar
EOF

#~# EXPECTED

<<~EOF
  foo
   bar
EOF

#~# ORIGINAL

<<~EOF
  #{1}
  #{2}
   bar
   baz
EOF

#~# EXPECTED

<<~EOF
  #{1}
  #{2}
   bar
   baz
EOF

#~# ORIGINAL

<<~EOF
  #{1}
   #{2}
   bar
    baz
EOF

#~# EXPECTED

<<~EOF
  #{1}
   #{2}
   bar
    baz
EOF

#~# ORIGINAL

<<~EOF
  #{1}
  foo
  #{2}
  bar
  #{3}
  baz
EOF

#~# EXPECTED

<<~EOF
  #{1}
  foo
  #{2}
  bar
  #{3}
  baz
EOF

#~# ORIGINAL

<<~EOF
  #{1}
   foo
  #{2}
    bar
  #{3}
     baz
EOF

#~# EXPECTED

<<~EOF
  #{1}
   foo
  #{2}
    bar
  #{3}
     baz
EOF

#~# ORIGINAL

begin
 <<~EOF
  foo
   bar
EOF
 end

#~# EXPECTED

begin
  <<~EOF
    foo
     bar
  EOF
end

#~# ORIGINAL heredoc_squiggly_no_leading_space

<<~EOF
a
EOF

#~# EXPECTED

<<~EOF
  a
EOF

#~# ORIGINAL heredoc_squiggly_extra_spaces

<<~EOF
#{1} #{2}
EOF

#~# EXPECTED

<<~EOF
#{1} #{2}
EOF

#~# ORIGINAL heredoc_squiggly_extra_spaces_2

<<~EOF
  #{1}      #{2}
EOF

#~# EXPECTED

<<~EOF
  #{1}      #{2}
EOF

#~# ORIGINAL heredoc_squiggly_extra_spaces_3

<<~EOF
  #{1}#{2}
EOF

#~# EXPECTED

<<~EOF
  #{1}#{2}
EOF

#~# ORIGINAL heredoc_squiggly_extra_spaces_4

<<~EOF
 #{1}#{2}
EOF

#~# EXPECTED

<<~EOF
  #{1}#{2}
EOF

#~# ORIGINAL heredoc_squigly_without_trailing_comma

a = {
  key: <<~EOF
    -----BEGIN PUBLIC KEY-----
    skldjflksdjlkfsdjlkfdsjlkfsd
    skdjlfjsdklfjslkdfjsdlkfjdsl
    -----END PUBLIC KEY-----
  EOF
}

#~# EXPECTED

a = {
  key: <<~EOF,
    -----BEGIN PUBLIC KEY-----
    skldjflksdjlkfsdjlkfdsjlkfsd
    skdjlfjsdklfjslkdfjsdlkfjdsl
    -----END PUBLIC KEY-----
  EOF
}

#~# ORIGINAL heredoc_squigly_with_trailing_comma

a = {
   key: <<~EOF,
    -----BEGIN PUBLIC KEY-----
    skldjflksdjlkfsdjlkfdsjlkfsd
    skdjlfjsdklfjslkdfjsdlkfjdsl
    -----END PUBLIC KEY-----
  EOF
}

#~# EXPECTED

a = {
  key: <<~EOF,
    -----BEGIN PUBLIC KEY-----
    skldjflksdjlkfsdjlkfdsjlkfsd
    skdjlfjsdklfjslkdfjsdlkfjdsl
    -----END PUBLIC KEY-----
  EOF
}

#~# ORIGINAL heredoc_squigly_with_trailing_comma_and_comment

a = {
  key: <<~EOF, # comment
    -----BEGIN PUBLIC KEY-----
    skldjflksdjlkfsdjlkfdsjlkfsd
    skdjlfjsdklfjslkdfjsdlkfjdsl
    -----END PUBLIC KEY-----
  EOF
}

#~# EXPECTED

a = {
  key: <<~EOF, # comment
    -----BEGIN PUBLIC KEY-----
    skldjflksdjlkfsdjlkfdsjlkfsd
    skdjlfjsdklfjslkdfjsdlkfjdsl
    -----END PUBLIC KEY-----
  EOF
}
