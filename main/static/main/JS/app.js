console.log("34242");

const TabsBut = document.querySelectorAll(".tabs__but");
const TabItem = document.querySelectorAll(".box--information")

console.log("34242");

TabsBut.forEach(function(item) {
	item.addEventListener("click", function() {
		let curr = item;
		let TabId = curr.getAttribute("data-tab");
		let CurrTab = document.querySelector(TabId);

		if (!curr.classList.contains("active")) {
			TabsBut.forEach(function(item) {
				item.classList.remove("active")
			});
	
			TabItem.forEach(function(item) {
				item.classList.remove("active")
			});
	
			curr.classList.add("active");
			CurrTab.classList.add("active");
		};
	});
});

document.getSelection("tabs__but").click()
