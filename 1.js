document.addEventListener("DOMContentLoaded", function () {
    fetch("../data/raw/data.csv")
        .then(response => response.text())
        .then(data => {
            let rows = data.split("\n").slice(1);
            let months = [];
            let dengueCases = [];
            let malariaCases = [];
            let chikungunyaCases = [];

            rows.forEach(row => {
                let cols = row.split(",");
                if (cols.length > 3) {
                    months.push(cols[0]);
                    dengueCases.push(parseInt(cols[1]) || 0);
                    malariaCases.push(parseInt(cols[2]) || 0);
                    chikungunyaCases.push(parseInt(cols[3]) || 0);
                }
            });

            let ctx = document.getElementById("casesChart").getContext("2d");
            new Chart(ctx, {
                type: "line",
                data: {
                    labels: months,
                    datasets: [
                        {
                            label: "Dengue Cases",
                            data: dengueCases,
                            borderColor: "red",
                            fill: false
                        },
                        {
                            label: "Malaria Cases",
                            data: malariaCases,
                            borderColor: "green",
                            fill: false
                        },
                        {
                            label: "Chikungunya Cases",
                            data: chikungunyaCases,
                            borderColor: "blue",
                            fill: false
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: "top"
                        }
                    }
                }
            });
        });
});
