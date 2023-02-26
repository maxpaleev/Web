
const TabsBtn = document.querySelectorAll(".tabs__but");
const TabItem = document.querySelectorAll(".box--information");

TabsBtn.forEach(function(item) {
	item.addEventListener("click", function() {
		let curr = item;
		let TabId = curr.getAttribute("data-tab");
		let CurrTab = document.querySelector(TabId);

		
		TabsBtn.forEach(function(item) {
			item.classList.remove("active")
		});

		TabItem.forEach(function(item) {
			item.classList.remove("active")
		});
	
		curr.classList.add("active");
		CurrTab.classList.remove("active")

	});
});

