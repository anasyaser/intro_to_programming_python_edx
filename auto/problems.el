(TeX-add-style-hook
 "problems"
 (lambda ()
   (add-to-list 'LaTeX-verbatim-environments-local "minted")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "array"
    "minted"))
 :latex)

