class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        memory = set([])
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = ''.join(local.split('.'))
            memory.add(local + '@' + domain)
        
        return len(memory)
