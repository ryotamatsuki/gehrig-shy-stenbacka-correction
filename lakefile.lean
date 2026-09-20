import Lake
open Lake DSL

package «gssCorrection» where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "b1007d8abfd0c776eb8a75e8f6bf26db5eae4a69"

@[default_target]
lean_lib GSSCorrection where
  srcDir := "formal"
