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

def smallbusinessadministrationsbasba504b(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration (SBA)</b></u><br>
    Capital Type: SBA 504B </center></p>
    <p><b><u>Introduction</u></b><br>
    The SBA 504 Loan is ideal for companies seeking long-term, fixed-rate financing for major fixed assets, such as owner-occupied commercial real estate or heavy machinery. It is designed so that a partnership between a private lender and a Certified Development Company (CDC) can help small businesses grow while preserving their working capital. {n} fits that definition. The 504 programs has been a staple of American economic development since its codification in 1958. In Fiscal Year 2024, the program reached a milestone of providing over $9 billion in specialized financing to thousands of growing businesses. By offering a low-down payment (typically only 10%), it allows entrepreneurs to "own instead of lease," building equity in their physical locations. Major projects often reach total financing of $5 million to $14 million, with the SBA-guaranteed portion (the debenture) usually capped at $5 million (or $5.5 million for manufacturers and energy-efficient projects). While the 504 loan offers stability through fixed interest rates and 25-year terms, its strict "owner-occupancy" requirements and lengthy application process (often 60–90 days) make it less suitable for quick-turnaround working capital needs.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. The SBA 504 Loan is a powerful public-private partnership. It is structured as a "three-part" loan: a conventional lender (usually a bank) provides 50% of the project cost, a CDC (an SBA-regulated nonprofit) provides 40% via a government-guaranteed debenture, and the borrower contributes the final 10%. This structure mitigates risk for the private lender while giving the small business access to "Wall Street" rates for their 40% portion. (SBA.gov, 2025)<br>
    <br>
    2. The best type of companies to raise money via the 504 program are for-profit, owner-occupied small businesses with a tangible net worth under $20 million and average net income below $6.5 million. It is a "brick-and-mortar" loan, specifically for purchasing land, existing buildings, or long-lived equipment. It is particularly popular for hotels, medical offices, and manufacturing plants where the business will occupy at least 51% of the space (or 60% for new construction). (NADCO, 2025)<br>
    <br>
    3. The 504 program emerged from Section 504 of the Small Business Investment Act of 1958. Over decades, it evolved from a simple community development tool into a sophisticated bond-funded program. In 2023 and 2024, significant updates were made to the program's "Standard Operating Procedures" (SOP 50 10 7 and 8), which streamlined the application process and expanded the "debt refinancing" capabilities, allowing businesses to refinance existing high-interest commercial debt into the 504 program. (Congressional Research Service, 2024)<br>
    <br>
    4. While the 504 loan offers low rates, there are specific compliance risks. Borrowers must meet job creation or retention goals—typically creating one job for every $95,000 borrowed (or $150,000 for manufacturers). Failure to meet occupancy standards (e.g., subletting too much of the building) can lead to a default. Additionally, while the interest rate is low, the "closing costs" and "CDC fees" can be higher upfront (2-3% of the loan) compared to traditional bank loans, though these fees can usually be financed into the loan. (Speritas Capital, 2025)<br>
    <br>
    5. To raise capital via an SBA 504 loan, a business owner must coordinate between their local bank and a CDC. The process involves a deep dive into the business's cash flow to ensure it can support the debt service. Because 504 loans are funded by monthly bond sales to investors, the interest rate for the CDC portion is not "locked in" until the loan actually funds (usually after construction or the purchase is complete), though it remains fixed for the life of the loan once set. (Capital CDC, 2025)
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Small Business Size – Tangible net worth <$20M and average net income <$6.5M.<br>
    · Owner-Occupancy – Must occupy 51% of an existing building or 60% of new construction.<br>
    · For-Profit Status – Non-profits and passive real estate investment firms are ineligible.<br>
    · Economic Development Goal – Must create/retain jobs or meet public policy goals (e.g., veteran-owned, rural location).<br>
    · U.S. Citizenship/Status – 100% of owners must be U.S. citizens, nationals, or Lawful Permanent Residents (as of 2025 SOP changes).<br>
    · "No Credit Elsewhere" – Must demonstrate that financing is not available on reasonable terms without the SBA guarantee.<br>
    · Character Eligibility – No "bad actor" events, pending convictions, or defaults on prior federal debt (student loans, etc.).<br>
    · Active Business – The business must be a legitimate operating entity, not a shell or speculative venture.
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    · Business Tax Returns – Full federal filings for the last 3 years.<br>
    · Personal Tax Returns – Last 3 years for all owners with 20% or more interest.<br>
    · Personal Financial Statement (SBA Form 413) – Current within 90 days.<br>
    · Interim Financial Statements – P&L and Balance Sheet within the last 60–120 days.<br>
    · Project Cost Breakdown – Executed purchase agreement or contractor estimates.<br>
    · Business Debt Schedule – List of all existing loans and notes payable.<br>
    · Resumes of Key Management – Showing expertise to run the business.<br>
    · Appraisal & Environmental Reports – Commissioned by the lender (Phase I Environmental is mandatory for real estate).<br>
    · Articles of Incorporation/Bylaws – Legal formation documents for the Operating Company.
    </p>
    <p><u><b>References</b></u><br>
    SBA.gov. (2025, June 03). 504 Loans: Long-term, fixed rate financing for major fixed assets. https://www.sba.gov/funding-programs/loans/504-loans<br>
    National Association of Development Companies (NADCO). (2025). What Is A 504 Loan? https://www.nadco.org/?page=whatis504<br>
    Congressional Research Service (CRS). (2024). SBA 504/CDC Loan Program Overview. https://crsreports.congress.gov/<br>
    Speritas Capital. (2025). SBA 504 Loan Program Explained - How it Works. https://www.speritascapital.com/commercial-financing/sba-504-loan-program-faqs<br>
    Capital CDC. (2025). SBA 504 Loan Eligibility Requirements. https://www.capitalcdc.com/sba-504-loans
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasba504bfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Small Business Administration (SBA)<br>
    SBA 504B</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is the SBA 504B loan program, and how does it differ from other SBA loans?</u></b><br>
    • Answer: The SBA 504B loan program is a long-term, fixed-rate financing option designed to help small businesses purchase major fixed assets such as real estate or heavy equipment, differing from SBA 7(a) loans by focusing specifically on asset acquisition rather than working capital.
    </p>
    <p><u><b>2. What types of businesses are best suited for SBA 504B financing?</u></b><br>
    • Answer: Established small businesses with stable cash flows that need to purchase or improve owner-occupied commercial real estate or long-term equipment are best suited for SBA 504B loans.
    </p>
    <p><u><b>3. How much funding can I receive through an SBA 504B loan?</u></b><br>
    • Answer: SBA 504B financing typically supports projects up to $5 million from the SBA portion, with higher limits for certain industries like manufacturing or energy projects.
    </p>
    <p><u><b>4. How is an SBA 504B loan structured?</u></b><br>
    • Answer: The loan is usually structured with 50% from a private lender, 40% from a Certified Development Company (CDC) backed by the SBA, and 10% from the borrower as equity.
    </p>
    <p><u><b>5. How quickly can I access capital through SBA 504B?</u></b><br>
    • Answer: Funding timelines generally range from 60 to 120 days, depending on documentation, appraisal, and SBA approval processes.
    </p>
    <p><u><b>6. What are the costs associated with SBA 504B loans?</u></b><br>
    • Answer: Costs include interest payments, SBA and CDC fees, closing costs, appraisal fees, and legal expenses, though rates are typically lower than conventional loans.
    </p>
    <p><u><b>7. Do I have to give up equity when using SBA 504B financing?</u></b><br>
    • Answer: No, SBA 504B loans are debt-based financing, allowing business owners to retain full ownership and control of their company.
    </p>
    <p><u><b>8. Can SBA 504B be combined with other financing sources?</u></b><br>
    • Answer: Yes, SBA 504B loans are often combined with bank loans, owner equity, or other government incentive programs to complete large projects.
    </p>
    <p><u><b>9. What are the key benefits of SBA 504B compared to conventional commercial loans?</u></b><br>
    • Answer: Key benefits include long repayment terms, fixed interest rates, lower down payments, and improved cash flow stability.
    </p>
    <p><u><b>10. What types of assets can be financed using SBA 504B?</u></b><br>
    • Answer: Eligible assets include owner-occupied commercial real estate, land improvements, construction, and long-term machinery or equipment.
    </p>
    <p><u><b>11. Are there any restrictions on how SBA 504B funds can be used?</u></b><br>
    • Answer: Yes, funds cannot be used for working capital, inventory, refinancing most existing debt, or investment properties.
    </p>
    <p><u><b>12. What risks are associated with SBA 504B financing?</u></b><br>
    • Answer: Risks include long approval timelines, strict eligibility requirements, collateral obligations, and long-term debt commitments.
    </p>
    <p><u><b>13. How does SBA 504B compare to SBA 7(a) loans?</u></b><br>
    • Answer: SBA 504B focuses on fixed-asset financing with lower fixed rates, while SBA 7(a) loans offer more flexibility for working capital and general business purposes.
    </p>
    <p><u><b>14. What types of businesses typically qualify for SBA 504B loans?</u></b><br>
    • Answer: Businesses that are for-profit, meet SBA size standards, occupy at least 51% of the property, and demonstrate repayment ability typically qualify.
    </p>
    <p><u><b>15. How can a business improve its chances of approval for an SBA 504B loan?</u></b><br>
    • Answer: Maintaining strong financial statements, good credit history, detailed project plans, and working with an experienced CDC and lender can significantly improve approval chances.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasba504btwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Small Business Administration (SBA)</b></u><br>
    Capital Type: SBA 504B</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    SBA 504B financing is best suited for established, growth-stage businesses that are expanding operations through fixed-asset purchases. Ideal candidates have operating history, stable cash flows, and a clear plan for long-term growth.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Eligible entities typically include C-Corps, LLCs, and S-Corps. Sole proprietorships and partnerships may qualify if they meet SBA eligibility rules, but incorporated entities are more commonly approved due to structure and compliance requirements.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Businesses are expected to demonstrate financial stability, adequate cash flow, and owner equity injection (commonly around 10%, with higher requirements for startups or special-purpose properties). Existing debt is reviewed as part of underwriting.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    This program operates within a government-backed lending framework, combining a private lender (bank), a Certified Development Company (CDC), and the SBA. Prior private or public funding does not disqualify participation.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    SBA 504B loans are designed for large, long-term capital needs, often ranging from hundreds of thousands to several million dollars, depending on project size, borrower eligibility, and SBA limits.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    This financing aligns with expansion or growth-stage capital, not early venture rounds. It is typically used alongside existing equity and bank participation rather than replacing traditional investment rounds.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Funds are generally released in structured tranches, tied to project milestones such as property acquisition, construction progress, or equipment installation. Final debenture funding occurs after project completion.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Funds are restricted to eligible fixed assets, including:<br>
    · Owner-occupied real estate<br>
    · Major equipment and machinery<br>
    · Construction, renovation, or modernization<br>
    · Working capital, inventory, and debt refinancing (outside program rules) are generally restricted.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk is moderate, as the loan is secured by fixed assets and supported by SBA guarantees. Businesses face repayment obligations and market risks but benefit from long-term fixed interest rates.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Capital cost is moderate, typically lower than conventional commercial real estate loans due to long-term fixed rates and SBA backing. There is no equity dilution, but long-term debt obligations apply.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs include CDC fees, SBA guaranty fees, legal fees, and appraisal costs. These are typically moderate and often financed into the loan rather than paid entirely out of pocket.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    The SBA 504B process typically takes 2–4 months, depending on project complexity, documentation readiness, and SBA approval timelines. Construction projects may take longer due to staged disbursements.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
