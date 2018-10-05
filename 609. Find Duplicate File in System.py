class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        res_files = []
        for directory in paths:
            files = directory.split()
            file_path = files[0]
            for file in files[1:]:
                file, content = self.getFileInfo(file)
                if content not in result.keys():
                    result[content] = [file_path + '/' + file]
                else:
                    result[content] += [file_path + '/' + file]

        
        for key, val in result.items():
            if len(val) > 1:
                res_files.append(val) 
        return res_files
    
    def getFileInfo(self, file):
        return file.split('(')
        file_name = file_contents[0]
        file_data = file_contents[1]
        return [file_name, file_data]
