document.addEventListener("DOMContentLoaded", () => {

    const tabButtons =
        document.querySelectorAll(".tab-button");

    const tabContents =
        document.querySelectorAll(".tab-content");


    tabButtons.forEach((button) => {

        button.addEventListener("click", () => {

            const selectedTab =
                button.dataset.tab;


            // Remove active state from buttons

            tabButtons.forEach((item) => {
                item.classList.remove("active");
            });


            // Hide all tab content

            tabContents.forEach((content) => {
                content.classList.remove("active");
            });


            // Activate selected button

            button.classList.add("active");


            // Show selected tab

            const selectedContent =
                document.getElementById(selectedTab);

            if (selectedContent) {
                selectedContent.classList.add("active");
            }

        });

    });

});