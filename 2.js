document.addEventListener("DOMContentLoaded", function () {
    fetch("../data/raw/data.csv")
        .then(response => response.text())
        .then(data => {
            let rows = data.split("\n").slice(1, 366); // First 365 rows
            let months = [];
            let dengueCases = [];
            let malariaCases = [];
            let chikungunyaCases = [];

            for (let i = 0; i < rows.length; i += 30) {
                let month = `Month ${Math.floor(i / 30) + 1}`;
                let dengueTotal = 0, malariaTotal = 0, chikungunyaTotal = 0;

                for (let j = i; j < i + 30 && j < rows.length; j++) {
                    let cols = rows[j].split(",");
                    dengueTotal += parseInt(cols[1]) || 0;
                    malariaTotal += parseInt(cols[2]) || 0;
                    chikungunyaTotal += parseInt(cols[3]) || 0;
                }

                months.push(month);
                dengueCases.push(dengueTotal);
                malariaCases.push(malariaTotal);
                chikungunyaCases.push(chikungunyaTotal);
            }

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
                    },
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: "Months"
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: "Total Cases"
                            }
                        }
                    }
                }
            });
        });
});
