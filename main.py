'''This algorithem hundles methematical computations in strings'''

def is_num(value):
	try:
		float(value)
		return True
	except:
		return False




def is_neg(value):
	if value < 0:
		return True
	else:
		return False




def is_math(expression, operators):
	c = 0
	if expression:
		for i in expression:
			if not c % 2:
				try:
					float(i)
				except:
					return False
			else:
				if i in operators:
					pass
				else:
					return False
			c += 1
		return True
	else:
		return False
		



class BitupleOverflow(Exception):
	pass




class Bituple:
	def __init__(self, bituple):
		if len(bituple) > 2:
			raise BitupleOverflow(f"Bituple length too big ({len(bituple)}), must be 2")
		else:
			self.bituple = bituple
	
	def first(self):
		return self.bituple[0]
		
	def last(self):
		return self.bituple[1]




class Listext(list):
	''' Listext (list extenssiom)'''
	def __init__(self, value):
		if type(value) == str:
			super().__init__(value.split(" "))
		else:
			super().__init__(value)
		self.__remove_spaces()
		
		
	def __remove_spaces(self):
		self.reduce([x for x in self if x], 0, len(self))
		
	
	def has(self, *args):
		for i in args:
			if i not in self:
				return False
		return True
		
		
	def is_homogeneous(self):
		t = None
		for i in self:
			if t == None:
				t = type(i)
			elif type(i) != t and t != None:
				return False
		return True
		
		
	def before(self, index):
		return self[index - 1]
		
		
	def after(self, index):
		return self[index + 1]
		
		
	def is_bound(self, index, *, left=False, right=False):
		if not right and not left:
			if self[index] == self.head() or self[index] == self.tail():
				return True
		elif right:
			if self[index] == self.tail():
				return True
		elif left:
			if self[index] == self.head():
				return True
		else:
			return False
		
		
	def reduce(self, value, start, stop):
		if type(value) == list:
			self[start:stop] = [*value]
		else:
			self[start:stop] = [value]
		
	
	def head(self):
		return self[0]
		
	
	def tail(self):
		return self[len(self) - 1]
		
	def where(self, value1, value2=None, *, s=None):
		if value1 in self:
			if not s:
				return self.index(value1)
			else:
				try:
					return self.index(value1, s)
				except:
					return -1
		elif value2 in self:
			if not s:
				return self.index(value2)
			else:
				return self.index(value2, s)
		else:
			return -1
	
	
	def rwhere(self, value1, value2):
		def inner(value):
			c = len(self) - 1
			for i in self:
				if self[c] == value:
					return c
				c -= 1
			return -1
			
		v1 = inner(value1)
		
		if is_neg(v1):
			return inner(value2)
		else:
			return v1
			
			
	def copy(self):
		return Listext(self)




class InStringMath:
	
	def __init__(self, expression):
		self.solvable = False
		self.operas = ["**", "^", "*", "×", "/", "÷",
		    "+", "-", "√"]
		self.answer = "0.0"
		self.start_pos = 0
		self.expression = self.__beautify(expression)
		if self.expression.tail() not in self.operas:
			self.brackets(self.expression)
		
		
	def __str__(self):
		return self.answer
		
		
	def __beautify(self, raw_expression):
		def beautify_str():
			beautiful_expr = ""
			c = 0
			for i in raw_expression:
				if i == "(":
					beautiful_expr += " " + i + " "
				elif i == ")":
					beautiful_expr += " " + i + " "
				elif i == "^":
					beautiful_expr += " " + i + " "
				elif i == "*" and raw_expression[c-1] == "*":
					beautiful_expr += i + " "
				elif i == "*" and raw_expression[c+1] == "*":
					beautiful_expr += " " + i
				elif i == "/":
					beautiful_expr += " " + i + " "
				elif i == "√":
					beautiful_expr += " " + i + " "
				else:
					beautiful_expr += i
				c += 1
			return beautiful_expr
		
		def beautify_listext(expression):
			expression = expression.split()
			c = 0
			for i in expression:
				if i == "(" and c != 0:
					if is_num(expression[c-1]):
						expression.insert(c, "*")
				elif i == ")" and c != len(expression) - 1:
					if is_num(expression[c+1]):
						expression.insert(c+1, "*")
				elif i == ")" and expression[c+1] == "(":
					vibrator.vibrate(.1)
					expression.insert(c+1, "*")
				c += 1
			return Listext(expression)
		
		if type(raw_expression) == str:
			raw_expression = beautify_str()
			raw_expression = beautify_listext(raw_expression)
		else:
			pass
		
		return Listext(raw_expression)
					
	
	
	def __brackets(self, expression):
		o_brac = expression.rwhere("(", "[")
		c_brac = expression.where(")", "]", s=o_brac)
		if not is_neg(o_brac) and not is_neg(c_brac):
			if is_math(expression[o_brac+1: c_brac],
			self.operas):
				ans = InStringMath(expression[o_brac+1: c_brac])
				print(ans.equals(), ["BRACKETS"])
				self.expression.reduce(str(ans), o_brac, c_brac+1)
				
				o_brac = self.expression.where("(", "[")
				c_brac = self.expression.where(")", "]")
					
				if not is_neg(o_brac + c_brac):
					self.__brackets(self.expression)
		
		o_brac = self.expression.where("(", "[")
		c_brac = self.expression.where(")", "]")
		
		if is_neg(o_brac) and is_neg(c_brac):
			self.no_brackets = True
		else:
			self.no_brackets = False
		
		
	def __exponent(self, expression):
		index = expression.where("**", "^")
		if not is_neg(index):
			if not expression.is_bound(index):
				before_sign = expression.before(index)
				after_sign = expression.after(index)
				if is_num(before_sign) and is_num(after_sign):
					ans = float(before_sign) ** float(after_sign)
					print(ans, "[EXPONENTIAL]")
					expression.reduce(str(ans), index-1, index+2)
					
			if not is_neg(self.expression.where("**", "^")):
				self.__exponent(self.expression)
		
		
	def __multiply_and_divide(self, expression):
		''' This method balances the prescedence of multilication and division. '''
		
		index1 = expression.where("*", "×")
		index2 = expression.where("/", "÷")
		
		if index1 != -1 and index2 == -1:
			index = index1
		elif index2 != -1 and index1 == -1:
			index = index2
		elif index1 != -1 and index2 != -1:
			if index1 < index2:
				index = index1
			else:
				index = index2
		else:
			index = -1
			
		if index == expression.where("*", "×"):
			self.__multiply(expression, index)
		elif index == expression.where("/", "÷"):
			self.__divide(expression, index)
			
		if not is_neg(index):
			self.__multiply_and_divide(self.expression)
		
		
	def __multiply(self, expression, index):
		if not expression.is_bound(index):
			before_sign = expression.before(index)
			after_sign = expression.after(index)
			if is_num(before_sign) and is_num(after_sign):
				ans = float(before_sign) * float(after_sign)
				print(ans, "[MULTIPLICATION]")
				expression.reduce(str(ans), index-1, index+2)
		
		
	def __divide(self, expression, index):
		if not expression.is_bound(index):
			before_sign = expression.before(index)
			after_sign = expression.after(index)
			if is_num(before_sign) and is_num(after_sign):
				ans = float(before_sign) / float(after_sign)
				print(ans, "[DIVISION]")
				expression.reduce(str(round(ans, 6)), index-1, index+2)
		
		
	def __add_and_substract(self, expression):
		''' This method balances the prescedence of addition and substruction. '''
		
		index1 = expression.where("+")
		index2 = expression.where("-")
		
		if not is_neg(index1) and is_neg(index2):
			index = index1
		elif not is_neg(index2) and is_neg(index1):
			index = index2
		elif not is_neg(index1) and not is_neg(index2):
			if index1 < index2:
				index = index1
			else:
				index = index2
		else:
			index = -1
			
		if index == expression.where("+"):
			self.__add(expression, index)
		elif index == expression.where("-"):
			self.__substract(expression, index)
			
		if not is_neg(index):
			self.__add_and_substract(self.expression)
		
		
	def __add(self, expression, index):
		if not expression.is_bound(index):
			before_sign = expression.before(index)
			after_sign = expression.after(index)
			if is_num(before_sign) and is_num(after_sign):
				ans = float(before_sign) + float(after_sign)
				print(ans, "[ADDITION]")
				expression.reduce(str(ans), index-1, index+2)
		
		
	def __substract(self, expression, index):
		if not expression.is_bound(index):
			before_sign = expression.before(index)
			after_sign = expression.after(index)
			if is_num(before_sign) and is_num(after_sign):
				ans = float(before_sign) - float(after_sign)
				print(ans, "[SUBSTRACT]")
				expression.reduce(str(ans), index-1, index+2)
				
				
	def __root(self, expression, index):
		if not expression.is_bound(index, right=True):
			before_sign = expression.before(index)
			after_sign = expression.after(index)
			if is_num(before_sign) and is_num(after_sign):
				ans = float(after_sign) ** (1 /float(before_sign))
				print(ans, "[R]")
				expression.reduce(str(ans), index-1, index+2)
			elif not is_num(before_sign) and is_num(after_sign):
				ans = float(after_sign) ** (1 / 2)
				print(ans, "[R]")
				expression.reduce(str(ans), index, index+2)
			
			
	def is_root(self, value):
		if value.startswith("√"):
			return True
		else:
			return False
			
			
	def equals(self):
		if self.solvable:
			return "{}".format(float(self.answer))
		else:
			return "_._"
		
		
	def brackets(self, expression):
		self.__brackets(expression)
		if self.no_brackets and is_math(expression, self.operas):
			self.exponential(expression)
		
		
	def exponential(self, expression):
		self.__exponent(expression)
		self.multiplication_and_division(expression)
		
		
	def multiplication_and_division(self, expression):
		self.__multiply_and_divide(expression)
		self.addition_and_substraction(expression)
		
		
	def addition_and_substraction(self, expression):
		self.__add_and_substract(expression)
		self.answer = self.expression[0]
		self.solvable = True
