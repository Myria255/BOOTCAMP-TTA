
import math


class Pagination():
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)
    
    def get_visible_items(self):
        start_idx = self.current_idx
        end_idx = min(start_idx + self.page_size, len(self.items))
        return self.items[start_idx:end_idx]
    def go_to_page(self, page_num):
        try:
            page_num = int(page_num)
            if 1 <= page_num <= self.total_pages:
                self.current_idx = (page_num - 1) * self.page_size
            else:
                raise ValueError("Invalid page number.")
        except ValueError:
            raise ValueError("Invalid page number. Please enter a valid integer.")
        return self
    
    def first_page(self):
        self.current_idx = 0
        return self
        
    def last_page(self):
        self.current_idx = (self.total_pages - 1) * self.page_size
        return self
    
    def next_page(self):
        if self.current_idx + self.page_size < len(self.items):
            self.current_idx += self.page_size
        return self

#Bonus 
    def __str__(self):
        return f"Pagination(items={self.items}, page_size={self.page_size}, current_idx={self.current_idx})" 
    
#Bonus 2
    
    def nextPage(self):
        return self.next_page()

    def prevPage(self):
        return self.previous_page()

    def getVisibleItems(self):
        return self.get_visible_items()

    def firstPage(self):
        return self.first_page()

    def lastPage(self):
        return self.last_page()

    def goToPage(self, page_num):
        return self.go_to_page(page_num)

    def previous_page(self):
        if self.current_idx - self.page_size >= 0:
            self.current_idx -= self.page_size
        return self
      
    
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 8)
print(str(p))

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print(e)

try:
    p.go_to_page(0)
except ValueError as e:
    print(e)

print(p.nextPage().nextPage().nextPage().getVisibleItems())
# ['m', 'n', 'o', 'p']