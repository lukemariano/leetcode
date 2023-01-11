// link para o problema:  https://leetcode.com/problems/same-tree/description/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  if (!p && !q) {
    return true;
  } else if ((p && !q) || (q && !p) || p.val !== q.val) {
    return false;
  }

  var pLeft = p.left ? p.left.val : null;
  var pRight = p.right ? p.right.val : null;
  var qLeft = q.left ? q.left.val : null;
  var qRight = q.right ? q.right.val : null;

  var pSizeRight = p.right ? Object.values(p.right).length : 0;
  var qSizeRight = q.right ? Object.values(q.right).length : 0;

  if (qSizeRight > 0 && pSizeRight > 0) {
    var list_nulls = [];
    let nulls = Object.values(p.right);

    list_nulls.push(nulls[1]);
    list_nulls.push(nulls[2]);

    if (list_nulls[0] === null && list_nulls[1] === null) {
      var output =
        p.val === q.val && pLeft === qLeft && pRight === qRight ? true : false;

      return output;
    }

    if (
      p.right.left !== null &&
      q.right.left !== null &&
      p.right.right !== null &&
      q.right.right !== null
    ) {
      return JSON.stringify(p) === JSON.stringify(q);
    }

    if (p.right.left !== null && q.right.left !== null) {
      let output_condition =
        p.val === q.val &&
        p.right.val === q.right.val &&
        p.right.left.val === q.right.left.val &&
        p.right.right === q.right.right
          ? true
          : false;

      return output_condition;
    }

    let output_condition =
      p.val === q.val &&
      p.right.val === q.right.val &&
      p.right.left === q.right.left &&
      p.right.right === q.right.right
        ? true
        : false;

    return output_condition;
  }

  // é preciso que o objeto não seja nulo para acessar os valores
  output =
    p.val === q.val && pLeft === qLeft && pRight === qRight ? true : false;

  return output;
};

// tentei ao máximo não usar JSON.stringify KKKKKKKKK
