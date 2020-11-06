static int treeDepth(TreeLinkNode root) {
    if (root != null) {
        int left = treeDepth(root.left);
        int right = treeDepth(root.right);
        return left > right ? left + 1 : right + 1;
    }
    return 0;
}


// 应用：平衡二叉树

private static boolean isBalanced(TreeLinkNode root) {
    if (root == null) {
        return true;
    }
    int left = treeDepth(root.left);
    int right = treeDepth(root.right);
    int diff=left-right;
    if(diff> 1||diff<-1){
        return false;
    }
    return isBalanced(root.left)&&isBalanced(root.right);
}