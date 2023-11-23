from util import filter_and_sort_emails,is_valid_email
 

n = int(input("Enter the number of emails: "))
emails = [input("Enter email: ") for _ in range(n)]

filtered_and_sorted_emails = filter_and_sort_emails(emails)

print("Filtered and sorted emails:")
print(filtered_and_sorted_emails)
