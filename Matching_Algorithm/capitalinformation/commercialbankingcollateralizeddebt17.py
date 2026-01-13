from django.shortcuts import render,HttpResponse,redirect
from django.utils.safestring import mark_safe
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared
from iquestions.models import IQuestions1,IQuestions2
from registration.models import User,UserDetail,UserDetail2
from connections.models import Match_Data
from datetime import datetime
from django.contrib.auth.decorators import login_required
from ..models import Capital_Matches,Matches_Purchased,Letter_Response,Purchases


def commercialbankingcollateralizeddebt(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Commercial Banking</b></u><br>
    Capital Type: Collateralized Debt</center></p>
    
    <p><b><u>Introduction</u></b><br>
    The global collateralized debt obligation market was valued at $27.5 billion in 2023, and is projected to reach $80.4 billion by 2033 <a href="https://www.alliedmarketresearch.com/collateralized-debt-obligation-market-A50930">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) A collateralized debt obligation (CDO) is a complex structured finance product that is backed by a pool of loans and other assets and sold to institutional investors. A CDO is a particular type of derivative because, as its name implies, its value is derived from another underlying asset. These assets become the collateral if the loan defaults. To create a CDO, investment banks gather cash flow-generating assets—such as mortgages, bonds, and other types of debt—and repackage them into discrete classes, or tranches based on the level of credit risk assumed by the investor. (Smith, 2021)

    <br><br>2) A collateralized debt obligation (CDO) is a complex structured finance product that is backed by a pool of loans and other assets and sold to institutional investors. Essentially, they are bundled debt resold to investors. The complicated nature of CDOs make them difficult to evaluate even for knowledgeable investors.
    <br>
    <br>The holder of the collateralized debt obligation can, in theory, collect the borrowed amount from the original borrower at the end of the loan period. A collateralized debt obligation is a type of derivative security because its price is derived from an underlying asset. Banks package together assets such as mortgages, bonds, or other types of asset-generating securities into discrete classes of investments. The classes are called tranches, which hold the cash flow of interest and principal payments in sequence, based on seniority.
    <br>
    <br>Banks generally sell CDOs to investors for three reasons. Funds from sales of collateralized debt obligations generate cash, which banks use to make new loans. The loan's risk of defaulting is transferred from the bank to the investors who purchase the CDO. And collateralized debt obligations are a relatively new type of security, created by banks to increase profits and (for public banks) increase their share price. (Fixed Income Securities (Bonds): Collateralized Debt Obligations, n.d.)
    <br>
    <br>3) Each type of CDO offers specific risks, from simpler structures like CLOs to more complex instruments like CDO-squared, that appeal to different kinds of investors seeking diversification. The types of CDOs are as follows:
    <br>    • Collateralized loan obligations (CLOs): These are backed primarily by corporate loans. Example: A CLO might contain loans made to various midsized companies across different industries.
    <br>    • Collateralized bond obligations (CBOs): These pool different types of bonds. Example: A CBO could include a mix of corporate bonds, municipal bonds, and emerging market bonds.
    <br>    • Synthetic CDOs: These use credit derivatives instead of actual debt. Example: A synthetic CDO might be based on credit default swaps for a group of companies, rather than their actual bonds.
    <br>    • Commercial real estate CDOs (CRE CDOs): These focus on commercial property debt. Example: A CRE CDO could contain loans for office buildings, shopping malls, and apartment complexes. (Tardi, 2024)
    <br>
    <br>4) Collateralized debt obligations allow banks to reduce the amount of risk they hold on their balance sheet. The majority of banks are required to hold a certain proportion of their assets in reserve. This incentivizes the securitization and sale of assets, as holding assets in reserves is costly for the banks. Collateralized debt obligations allow banks to transform a relatively illiquid security (a single bond or loan) into a relatively liquid security. (Team, n.d.)
    <br>
    <br>5) Banks are able to lower the amount of risk they have on their balance sheet by using collateralized loan obligations. Most banks are required to retain a specific amount of assets in reserve. This encourages the securitization and sale of assets because it is expensive for banks to maintain assets in reserves. Banks can turn a single bond or loan, which is generally illiquid, into a very liquid instrument by using collateralized debt obligations. The pool may contain corporate bonds, government bonds, and assets backed by mortgages. CBOs are frequently utilized as interest rate risk protection. (Collateralized Debt Obligation Market Size, Share, Growth, and Industry Analysis by Type (Collateralized loan obligations (CLOs), Collateralized bond obligations (CBOs), Collateralized synthetic obligations (CSOs), and Structured finance CDOs (SFCDOs)) By, 2025)
    </p>
                             
    <u><b><p>References</u></b><br>
    Collateralized Debt Obligation Market Size, Share, Growth, and Industry Analysis by Type (Collateralized loan obligations (CLOs), Collateralized bond obligations (CBOs), Collateralized synthetic obligations (CSOs), and Structured finance CDOs (SFCDOs)) By. (2025, January 6). Retrieved from Business Research Insights : <a href="https://www.businessresearchinsights.com/market-reports/collateralized-debt-obligation-market-102741">https://www.businessresearchinsights.com/market-reports/collateralized-debt-obligation-market-102741</a>
    <br><br>Fixed Income Securities (Bonds): Collateralized Debt Obligations. (n.d.). Retrieved from New York Public Library: <a href="https://libguides.nypl.org/c.php?g=1043575&p=7660195">https://libguides.nypl.org/c.php?g=1043575&p=7660195</a>
    <br><br>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press .
    <br><br>Tardi, C. (2024, October 1). Collateralized Debt Obligation (CDO): What It Is and How It Works. Retrieved from Investopedia: <a href="https://www.investopedia.com/terms/c/cdo.asp">https://www.investopedia.com/terms/c/cdo.asp</a>
    <br><br>Team, C. (n.d.). Collateralized Debt Obligation (CDO). Retrieved from CFI: <a href="https://corporatefinanceinstitute.com/resources/fixed-income/collateralized-debt-obligation-cdo/">https://corporatefinanceinstitute.com/resources/fixed-income/collateralized-debt-obligation-cdo/</a>
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Legal Entity Status: Must be a recognized legal entity (e.g., corporation, LLC).
    <br>• Ownership of Collateral: Must have clear ownership of assets used as collateral.
    <br>• Regulatory Compliance: Must comply with all relevant local, state, and federal laws.
    <br>• Authority to Pledge Assets: Must have the legal authority to pledge assets as collateral.
    <br>• No Restrictions on Borrowing: Must not face legal or regulatory restrictions on borrowing.
    <br>• Good Standing with Credit Agencies: Must have a stable financial history and good standing with credit agencies.
    <br>• Corporate Governance: Must have proper governance and documentation for borrowing.
    <br>• Financial Documentation: Must provide accurate financial statements and documentation.
    <br>• No Pending Litigation: Should not be involved in legal disputes affecting financial health.
    <br>• Insurance on Collateral: May need to insure collateral to protect its value.
    <br>• Valid Collateral Documentation: Must provide valid documents proving ownership and value of the collateral.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Formation Documents: Articles of Incorporation, Operating Agreement, or Partnership Agreement.
    <br>• Proof of Ownership of Collateral: Deeds, Titles, Bills of Sale, or Appraisal Reports for pledged assets.
    <br>• Financial Statements: Balance Sheets, Income Statements, Cash Flow Statements, and Interim Financial Statements.
    <br>• Tax Returns: Business and Personal Tax Returns (last 2-3 years).
    <br>• Credit Reports: Business and Personal Credit Reports (if applicable).
    <br>• Collateral Insurance Documentation: Proof of insurance for the pledged assets.
    <br>• Loan Application Form: Completed form provided by the lender to begin the process.
    <br>• Personal Guarantees: Personal Guarantee Form (if required).
    <br>• Legal Compliance Documents: Business Licenses, Permits, and Certificates of Good Standing.
    <br>• Borrower’s Certificate or Resolution: Board Resolution or Written Consent for loan authorization.
    <br>• Financial Projections: Projections or Business Plan (for startups or businesses with limited history).
    <br>• Loan Agreement and Terms: Draft Loan Agreement or Term Sheet outlining loan specifics.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingcollateralizeddebtfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Commercial Banking<br>
    Capital Type: Collateralized Debt</center></p>                        
    <p><center><u><b>Frequently Asked Question for Commercial Banking Collateralized Debt</u></b></center></p>
    <p><u><b>1. What is Collateralized Debt?</u></b><br>
    • Answer: Collateralized debt refers to loans or credit lines that are secured by specific assets or collateral, such as property, equipment, or inventory. If the borrower defaults, the lender has the right to seize the collateral to recover the loan amount.
    </p>
                             
    <p><u><b>2. What types of assets can be used as collateral?</u></b><br>
    • Answer: Common assets used as collateral include real estate, accounts receivable, inventory, machinery, and even intellectual property. The asset must have enough value to cover the loan amount if the borrower defaults.
    </p>
                             
    <p><u><b>3. How does collateralized debt differ from unsecured debt?</u></b><br>
    • Answer: Unlike unsecured debt, which doesn’t require collateral, collateralized debt involves pledging specific assets as security for the loan. This generally lowers the risk for lenders, potentially leading to better loan terms for borrowers.
    </p>
                             
    <p><u><b>4. Why would my business choose collateralized debt over other financing options?</u></b><br>
    • Answer:
    Collateralized debt can offer lower interest rates, higher borrowing limits, and greater flexibility than unsecured debt or alternative financing options like equity financing. It’s particularly useful for businesses with valuable assets but limited cash flow.
    </p>
                             
    <p><u><b>5. What are the advantages of using collateralized debt?</u></b><br>
    • Answer:
    The primary advantages include lower interest rates, larger loan amounts, and the ability to secure funding quickly, especially if your business has strong assets. Additionally, it allows businesses to maintain ownership without giving up equity.
    </p>
                             
    <p><u><b>6. What are the risks of using collateralized debt?</u></b><br>
    • Answer: The main risk is that if the business defaults on the loan, the lender can seize the pledged collateral, which could include essential assets. It’s crucial to have a solid repayment plan to mitigate this risk.</p>
                             
    <p><u><b>7. What kind of businesses are eligible for collateralized debt?</u></b><br>
    • Answer: Collateralized debt is suitable for businesses with valuable tangible assets, such as manufacturers, distributors, or real estate businesses. Companies with assets like equipment, inventory, or receivables are well-positioned for this type of financing.</p>
                             
    <p><u><b>8. How much can my business borrow through collateralized debt?</u></b><br>
    • Answer: The amount a business can borrow depends on the value of the assets used as collateral. Lenders typically offer a percentage of the collateral’s value, often between 50-80% for inventory or receivables and 70-90% for real estate or machinery.</p>
                             
    <p><u><b>9. What happens if the value of my collateral decreases after I secure the loan?</u></b><br>
    • Answer: If the value of the collateral decreases significantly, the lender may require additional collateral to secure the loan or adjust the loan terms. It’s important to monitor the value of the collateral and maintain adequate protection for the loan.</p>
                             
    <p><u><b>10. How do lenders determine the value of collateral?</u></b><br>
    • Answer: Lenders typically assess collateral through appraisals, audits, or valuations to determine its market value. This process helps establish the loan-to-value ratio and ensures that the collateral is sufficient to cover the loan.</p>
                             
    <p><u><b>11. What fees are associated with collateralized debt?</u></b><br>
    • Answer: Fees can include appraisal fees, legal fees, underwriting fees, and ongoing monitoring fees. Some lenders may also charge for loan setup or modification. Understanding these fees upfront helps businesses gauge the total cost of the loan.</p>
                             
    <p><u><b>12. Can my business still get collateralized debt with bad credit?</u></b><br>
    • Answer: Yes, businesses with poor credit may still be eligible for collateralized debt if they have strong, valuable assets. Since the loan is secured by collateral, the lender's risk is reduced, which can help offset credit concerns.
    </p> 
                             
    <p><u><b>13. How long does it take to get approval for collateralized debt?</u></b><br>
    • Answer: Approval timelines can vary, but it is generally faster than traditional loans. If the required documentation is in order and the collateral’s value is clear, approval can occur within a few weeks. However, complex or high-value collateral may require longer processing times.</p>
    
    <p><u><b>14. What are the typical terms of collateralized debt loans?</u></b><br>
    • Answer: Terms can vary widely but typically include a fixed or variable interest rate, repayment schedule (e.g., monthly, quarterly), and loan maturity (e.g., 1-5 years). The length of the loan term and the interest rate will depend on the value of the collateral and the business’s financial health.</p>
    
    <p><u><b>15. Can I use multiple types of collateral for a single loan?</u></b><br>
    • Answer: Yes, businesses can use a combination of assets as collateral to secure a loan. This is known as multi-collateral lending and can help increase the loan amount or provide additional security for the lender.</p>
    
     <p><u><b>16. What happens if I can’t repay the loan?</u></b><br>
    • Answer: If the business defaults on a collateralized debt loan, the lender has the right to seize the pledged collateral to recover the loan amount. This can result in the loss of critical assets, so it’s essential to have a solid repayment plan in place.</p>
    
     <p><u><b>17. Is collateralized debt a good option for a growing business?</u></b><br>
    • Answer: Yes, it can be an excellent option for growing businesses that have valuable assets but may not have sufficient cash flow or a strong credit history. It provides an opportunity to unlock capital for expansion or operations while retaining ownership.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def commercialbankingcollateralizeddebttwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    introduction = """
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR</b></u><br>
    Commercial Banking Collateralized Debt</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    Mature or growing businesses with a strong asset base and established operations are best positioned to use collateralized debt as a financing tool.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Corporations (C-Corp or S-Corp) and LLCs are ideal for collateralized debt as they can pledge assets and provide clear ownership and governance. LLCs offer flexibility and limited liability, making them attractive to lenders. Partnerships may qualify if they have significant assets and a clear structure but face challenges due to shared liability. Sole proprietorships are less common for collateralized debt due to their limited legal structure and lack of asset protection.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    There are no strict rules based on the amount of pre-capital raised but lenders will carefully evaluate a business’s overall financial health, existing debt obligations, and asset quality before approving collateralized debt.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While there are no hard and fast restrictions solely based on how pre-capital is raised, factors such as existing debt obligations, equity financing agreements, restrictive covenants, and overall financial health can influence a company's ability to qualify for and successfully use collateralized debt.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Businesses can raise a significant amount of capital using collateralized debt, often in the range of 50-90% of the value of their collateral, depending on the asset type and the terms of the loan.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Series B and later rounds are ideal for collateralized debt, as the company has usually reached a level of stability with enough assets to leverage while still needing capital for further growth.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    The typical number of tranches in a Collateralized Debt arrangement usually ranges from one to three tranches, though more can be structured depending on the complexity of the loan and the business's needs.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Funds from Collateralized Debt are primarily intended for business purposes like operational expenses, growth, or acquisitions. While there is often significant flexibility, companies should be mindful of any restrictions outlined in the loan agreement, particularly around the usage of funds and financial covenants. 
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Businesses need a moderate to high risk tolerance to pursue collateralized debt, given the potential for asset loss, debt obligations, and operational constraints. Companies should have a solid financial foundation, predictable cash flow, and a clear risk management strategy to navigate the potential challenges associated with this type of financing. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    A business considering collateralized debt must have a moderate to high tolerance for capital costs, as it involves not only interest payments but also upfront fees, ongoing management costs, and potential penalties.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Businesses should budget for 1% to 5% of the loan amount in upfront costs when using Collateralized Debt, though the exact amount will vary based on the loan size, type of collateral, and the specific terms of the loan. These costs may include due diligence, legal fees, appraisals, and other administrative expenses.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    A company can generally expect to receive capital from Collateralized Debt within 2 to 6 weeks, but the exact timeline can vary based on the loan's complexity, collateral type, and the efficiency of both the borrower and lender in completing the necessary steps.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)