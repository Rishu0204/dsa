class Solution {
    boolean board[][];
    public int totalNQueens(int n) {
        board=new boolean[n][n];
        return countQueenpos(0,n);
    }
    
    
    public boolean safePlace(int row,int col){
        //Top queen check
        for(int i=row;i>=0;i--){
            if(board[i][col]==true){
                return false;
            }
        }
        
        //Left Queen check
        for(int i=row,j=col;i>=0 && j>=0;i--,j--){
            if(board[i][j]==true){
                return false;
            }
        }
        
        //right quuen check
        for(int i=row,j=col;i>=0 && j<board[0].length;i--,j++){
            if(board[i][j]==true){
                return false;
            }
        }
        return true;
    }
    
    
    public int countQueenpos(int row, int n){
        if (row==n){
            return 1;
        }
        int count =0;
        for(int col=0;col<n;col++){
            if(safePlace(row,col)){
                board[row][col]=true;
                count=count+countQueenpos(row+1,n);
                board[row][col]=false;
            }
        }
        return count;
    }
}