class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        
        row = len(image)
        col = len(image[0])
        
        orginial = image[sr][sc]

        
        def dfs(image, orginial, sr, sc, row, col, color):
            if sr<0 or sr>= row or sc <0 or sc>= col:
                return
            if image[sr][sc] != orginial:
                return 
            
            
            image[sr][sc] = color
                
            dfs(image, orginial, sr+1, sc, row, col, color)
            dfs(image, orginial, sr-1, sc, row, col, color)
            dfs(image, orginial, sr, sc+1, row, col, color)
            dfs(image, orginial, sr, sc-1, row, col, color)
        
        dfs(image, orginial, sr, sc, row, col, color)
        return image
        
        
                
            
            