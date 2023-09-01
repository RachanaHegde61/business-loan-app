document.addEventListener("DOMContentLoaded", () => {
  const submitBtn = document.getElementById("submitBtn");
  const resultDiv = document.getElementById("result");

  submitBtn.addEventListener("click", async (event) => {
      event.preventDefault();

      const applicationData = {
          business_name: "XYZ Corp",
          year_established: 2010,
          loan_amount: 80000,
          accounting_provider: "MYOB",
          balance_sheet: [
              {"year": 2021, "month": 7, "profitOrLoss": -5000, "assetsValue": 150000},
              // ... other balance sheet entries ...
          ],
      };

      try {
          const response = await fetch("/submit_application", {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: JSON.stringify(applicationData),
          });

          const data = await response.json();

          // Display the application result
          resultDiv.innerHTML = `
Application Result:
Business Name: ${data.business_name}
Year Established: ${data.year_established}
Pre-Assessment: ${data.pre_assessment}%
Decision Outcome: ${data.decision_outcome}`;
      } catch (error) {
          console.error("Error:", error);
          resultDiv.textContent = "An error occurred while submitting the application.";
      }
  });
});
