
monthConversions = {
  'Jan': 'January',
  'Feb': 'Febrary',
  'Mar': 'March',
  'Apr': 'April',
  'May': 'May',
  'Jun': 'June',
  'Jul': 'July',
  'Aug': 'August',
  'Sep': 'September',
  'Oct': 'October',
  'Nov': 'November',
  'Dec': 'December',  
}

print(monthConversions['Nov'])

print(monthConversions.get('Mar'))

print(monthConversions.get('Luv', 'Not Valid Key'))
