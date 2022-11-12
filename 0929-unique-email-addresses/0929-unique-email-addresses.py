class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            email = email.split('@')
            local = email[0].replace('.', '').split('+')[0]
            domain = email[1]
            unique.add(local + '@' + domain)
        return len(unique)