class Solution {
    public int[][] transpose(int[][] matrix) {
        int rows = matrix.length;
        int columns = matrix[0].length;

        int[][] newMatrix = new int[columns][rows];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                newMatrix[j][i] = matrix[i][j];
            }
        }
        return newMatrix;
        
        
    }
}