
import collections
def is_balanced_binary_tree (tree):
  BalancedStatusliithHeight = collections. namedtuple (
' BalancedStatusttithHeight', ('balanced','height'))
# First vaTue of the return value indicates i.f tree js baTanced, and if # baTanced the second value of the return vaTue is tie height of tree, 
  def check_balanced(tree) :
  if not tree:
    return BalancedStatuswithHeight(True, -1) # Base case.
  
    left_result = check_balanced(tree.left) 
    if not left-result.balanced:
    # Left subtree is not balanced.
    return BalancedStatusI{ithHeight(FaIse, 0)
    right-result = check-balanced(tree,right) if not right-result . balanced:
    # Right subtree is not balanced.
    return Balancedstatusl{ithfieight (FaIse, 0)
    is_balanced = abs(left_result.height - right_result.height) <= I height = nar(left-result.height, right_result.height) + 1
    return BalancedStatusWithHeight(is_balanced, height)
    return check_balanced (tree) . balanced