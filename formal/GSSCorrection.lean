import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace GSSCorrection

/-!
Targeted formal verification for the Gehrig–Shy–Stenbacka correction note.

Model boundary:
* The Stage-4A clean-room audit certifies the economic case partition and
  branch exhaustiveness.
* This file certifies the proof-critical algebraic reductions, domain
  containment, welfare identities, and exact rational counterexamples.
* It does not claim a formalization of the complete equilibrium
  correspondence or game-wide uniqueness.
-/

noncomputable section

open Real

def hbpLower (r s : ℝ) : ℝ :=
  -3 + ((4 - r^2 + 3*r) / 4) * s

def uniformLower (r s : ℝ) : ℝ :=
  -3 + ((2 + r^2 + 3*r) / 2) * s

def hbpUpperQ (q s : ℝ) : ℝ :=
  3 - (q^2 / 2) * s

def uniformUpperQ (q s : ℝ) : ℝ :=
  3 - ((q^2 + 3*q) / 2) * s

/-- HBP entrant: high-segment-only comparison gap, with r = sqrt(theta). -/
def hbpBGap (r s d : ℝ) : ℝ :=
  let θ := r^2
  let pA := 1 + ((2 + θ) * s + 4*d) / 6
  let qA := 1 + (4*d - (1 - θ) * s) / 6
  let hOld := 1 + pA - s
  let hNew := 1 + qA
  let hBar := (1 - θ) * hOld + θ * hNew
  hBar - r * hNew

/-- Uniform entrant: high-new-segment-only comparison gap. -/
def uniformBGap (r s d : ℝ) : ℝ :=
  let θ := r^2
  let pA := 1 + (2*d + (1 - θ) * s) / 3
  let hOld := 1 + pA - s
  let hNew := 1 + pA
  let hBar := (1 - θ) * hOld + θ * hNew
  hBar - r * hNew

/-- Uniform incumbent: high-old-segment-only comparison gap,
    with q = sqrt(1-theta). -/
def uniformAGap (q s d : ℝ) : ℝ :=
  let oldWeight := q^2
  let pB := 1 + (d - oldWeight * s) / 3
  let hOld := 1 + pB + s - d
  let hNew := 1 + pB - d
  let hBar := oldWeight * hOld + (1 - oldWeight) * hNew
  hBar - q * hOld

theorem hbpBGap_normal_form (r s d : ℝ) :
    hbpBGap r s d = (2/3 : ℝ) * (1-r) * (d - hbpLower r s) := by
  unfold hbpBGap hbpLower
  ring

theorem uniformBGap_normal_form (r s d : ℝ) :
    uniformBGap r s d =
      (2/3 : ℝ) * (1-r) * (d - uniformLower r s) := by
  unfold uniformBGap uniformLower
  ring

theorem uniformAGap_normal_form (q s d : ℝ) :
    uniformAGap q s d =
      (2/3 : ℝ) * (1-q) * (uniformUpperQ q s - d) := by
  unfold uniformAGap uniformUpperQ
  ring

theorem hbp_lower_threshold_sufficient
    (r s d : ℝ) (hr : r < 1) (hdom : hbpLower r s ≤ d) :
    0 ≤ hbpBGap r s d := by
  rw [hbpBGap_normal_form]
  have hp : 0 ≤ (2/3 : ℝ) * (1-r) := by
    positivity
  exact mul_nonneg hp (sub_nonneg.mpr hdom)

theorem hbp_lower_threshold_necessary
    (r s d : ℝ) (hr : r < 1) (hgap : 0 ≤ hbpBGap r s d) :
    hbpLower r s ≤ d := by
  rw [hbpBGap_normal_form] at hgap
  by_contra h
  have hd : d < hbpLower r s := lt_of_not_ge h
  have hp : 0 < (2/3 : ℝ) * (1-r) := by
    positivity
  have hn : (2/3 : ℝ) * (1-r) * (d - hbpLower r s) < 0 := by
    exact mul_neg_of_pos_of_neg hp (sub_neg.mpr hd)
  linarith

theorem uniform_lower_threshold_sufficient
    (r s d : ℝ) (hr : r < 1) (hdom : uniformLower r s ≤ d) :
    0 ≤ uniformBGap r s d := by
  rw [uniformBGap_normal_form]
  have hp : 0 ≤ (2/3 : ℝ) * (1-r) := by
    positivity
  exact mul_nonneg hp (sub_nonneg.mpr hdom)

theorem uniform_lower_threshold_necessary
    (r s d : ℝ) (hr : r < 1) (hgap : 0 ≤ uniformBGap r s d) :
    uniformLower r s ≤ d := by
  rw [uniformBGap_normal_form] at hgap
  by_contra h
  have hd : d < uniformLower r s := lt_of_not_ge h
  have hp : 0 < (2/3 : ℝ) * (1-r) := by
    positivity
  have hn : (2/3 : ℝ) * (1-r) * (d - uniformLower r s) < 0 := by
    exact mul_neg_of_pos_of_neg hp (sub_neg.mpr hd)
  linarith

theorem uniform_upper_threshold_sufficient
    (q s d : ℝ) (hq : q < 1) (hdom : d ≤ uniformUpperQ q s) :
    0 ≤ uniformAGap q s d := by
  rw [uniformAGap_normal_form]
  have hp : 0 ≤ (2/3 : ℝ) * (1-q) := by
    positivity
  exact mul_nonneg hp (sub_nonneg.mpr hdom)

theorem uniform_upper_threshold_necessary
    (q s d : ℝ) (hq : q < 1) (hgap : 0 ≤ uniformAGap q s d) :
    d ≤ uniformUpperQ q s := by
  rw [uniformAGap_normal_form] at hgap
  by_contra h
  have hd : uniformUpperQ q s < d := lt_of_not_ge h
  have hp : 0 < (2/3 : ℝ) * (1-q) := by
    positivity
  have hn : (2/3 : ℝ) * (1-q) * (uniformUpperQ q s - d) < 0 := by
    exact mul_neg_of_pos_of_neg hp (sub_neg.mpr hd)
  linarith

/-- P3 lower-bound containment, using r = sqrt(theta) ≥ 0. -/
theorem p3_lower_containment
    (r s : ℝ) (hr : 0 ≤ r) (hs : 0 ≤ s) :
    hbpLower r s ≤ uniformLower r s := by
  unfold hbpLower uniformLower
  have hsum : 0 ≤ r^2 + r := by positivity
  have hprod : 0 ≤ s * (r^2 + r) := mul_nonneg hs hsum
  nlinarith

/-- P3 upper-bound containment, using q = sqrt(1-theta) ≥ 0. -/
theorem p3_upper_containment
    (q s : ℝ) (hq : 0 ≤ q) (hs : 0 ≤ s) :
    uniformUpperQ q s ≤ hbpUpperQ q s := by
  unfold uniformUpperQ hbpUpperQ
  have hprod : 0 ≤ s * q := mul_nonneg hs hq
  nlinarith

def welfareGap (θ σ τ : ℝ) : ℝ :=
  -(θ * (1-θ) * σ^2) / (16*τ)

theorem p4_welfare_accounting
    (θ σ τ : ℝ) (hτ : τ ≠ 0) :
    -(3 * θ * (1-θ) * σ^2) / (16*τ)
      + (θ * (1-θ) * σ^2) / (8*τ)
      = welfareGap θ σ τ := by
  unfold welfareGap
  field_simp [hτ]
  ring

theorem p4_resource_decomposition
    (θ σ τ : ℝ) (hτ : τ ≠ 0) :
    -(3 * θ * (1-θ) * σ^2) / (16*τ)
      + (4 * θ * (1-θ) * σ^2) / (16*τ)
      = -welfareGap θ σ τ := by
  unfold welfareGap
  field_simp [hτ]
  ring

theorem p4_welfare_negative
    (θ σ τ : ℝ)
    (hθ0 : 0 < θ) (hθ1 : θ < 1) (hσ : 0 < σ) (hτ : 0 < τ) :
    welfareGap θ σ τ < 0 := by
  unfold welfareGap
  have hcohort : 0 < 1 - θ := sub_pos.mpr hθ1
  have hsquare : 0 < σ^2 := pow_pos hσ 2
  have hnum : 0 < θ * (1-θ) * σ^2 :=
    mul_pos (mul_pos hθ0 hcohort) hsquare
  have hneg : -(θ * (1-θ) * σ^2) < 0 := neg_lt_zero.mpr hnum
  have hden : 0 < 16 * τ := mul_pos (by norm_num) hτ
  rw [div_eq_mul_inv]
  exact mul_neg_of_neg_of_pos hneg (inv_pos.mpr hden)

/-- CE1: exact HBP entrant deviation gain. -/
theorem ce1_hbp_gain :
    ((217 : ℚ) / 240) * ((1 : ℚ) / 2 * ((217 : ℚ) / 480))
      - ((37 : ℚ) / 60) *
        (((1 : ℚ) / 2) * ((1 : ℚ) / 48)
          + ((1 : ℚ) / 2) * ((143 : ℚ) / 240))
      = (3281 : ℚ) / 230400 := by
  norm_num

theorem ce1_hbp_gain_positive : (0 : ℚ) < (3281 : ℚ) / 230400 := by
  norm_num

/-- CE2: exact uniform entrant new-only deviation gain. -/
theorem ce2_uniform_entrant_gain :
    ((49 : ℚ) / 60) * ((1 : ℚ) / 2 * ((49 : ℚ) / 120))
      - ((17 : ℚ) / 30) *
        (((1 : ℚ) / 2) * ((1 : ℚ) / 30)
          + ((1 : ℚ) / 2) * ((8 : ℚ) / 15))
      = (89 : ℚ) / 14400 := by
  norm_num

theorem ce2_uniform_entrant_gain_positive :
    (0 : ℚ) < (89 : ℚ) / 14400 := by
  norm_num

/-- CE3: exact uniform incumbent old-only deviation gain. -/
theorem ce3_uniform_incumbent_gain :
    ((49 : ℚ) / 60) * ((1 : ℚ) / 2 * ((49 : ℚ) / 120))
      - ((17 : ℚ) / 30) * ((17 : ℚ) / 60)
      = (89 : ℚ) / 14400 := by
  norm_num

theorem ce3_uniform_incumbent_gain_positive :
    (0 : ℚ) < (89 : ℚ) / 14400 := by
  norm_num

#print axioms hbpBGap_normal_form
#print axioms uniformBGap_normal_form
#print axioms uniformAGap_normal_form
#print axioms p3_lower_containment
#print axioms p3_upper_containment
#print axioms p4_welfare_accounting
#print axioms p4_resource_decomposition
#print axioms p4_welfare_negative
#print axioms ce1_hbp_gain
#print axioms ce2_uniform_entrant_gain
#print axioms ce3_uniform_incumbent_gain

end

end GSSCorrection
