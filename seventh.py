import re

emails = ['abc@gmail.com', '123$tt*@xyz.com', 'good@bad@uk.in', 'nasa@usa12.space', 'no-reply@domain.in', 'ramhanuman@saketa.lok', 'ruhi.mohan@exter123.123', 'fake@fake123.fakercom']
regExp = '^[a-zA-Z_-].([a-zA-Z0-9_-])*@[a-zA-Z0-9]*\.[a-zA-Z]{2,5}$'
valid_emails = [email for email in emails if re.match(regExp,email)]

print(valid_emails)