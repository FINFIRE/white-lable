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

def privatedebtrealestateloan(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Real Estate Loan </center></p>
    <p><b><u>Introduction</u></b><br>
    Private Real Estate Loans—often referred to as "Hard Money" or "Bridge Loans"—are ideal for companies seeking rapid financing for property acquisitions, renovations, or distressed asset stabilization. They are designed so that private investment firms and high-net-worth individuals can provide capital based on the value of the real estate rather than the borrower's personal credit or historical tax returns. {n} fits that definition. In 2026, the private debt market for real estate has surged as traditional banks have tightened lending standards. Private lenders like Blackstone and specialized "Hard Money" shops provide the speed necessary to win competitive bids. Unlike a 30-year bank mortgage, these are short-term instruments, typically lasting 12 to 36 months. On average, private real estate loans cover 60% to 75% of the "After Repair Value" (ARV), with interest rates ranging from 9% to 14%, depending on the project's risk profile. While private debt offers a path to closing deals in days rather than months, the high cost of capital and the risk of "predatory" foreclosure terms if a project exceeds its timeline make it a tool best suited for experienced developers with a clear exit strategy.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. A Private Real Estate Loan is a non-bank loan secured by a first-priority lien on a specific property. Because the lender's primary protection is the "collateral," they are less concerned with the borrower's Debt-to-Income (DTI) ratio and more focused on the Loan-to-Value (LTV) ratio. These loans are often "interest-only," meaning the principal is paid back in one lump sum at the end of the term. (Investopedia, 2026)<br>
    <br>2. The best type of companies to raise capital via private real estate debt are "fix-and-flip" developers, commercial investors looking to "bridge" the gap before a permanent refinance, and businesses needing to unlock equity in their existing property to fund operations. It is particularly effective for properties that do not yet meet the occupancy or condition requirements for traditional bank financing. (Forbes, 2025)<br>
    <br>3. Private real estate lending emerged as a formalized alternative after the 2008 financial crisis, when bank regulations (like Dodd-Frank) made it difficult for entrepreneurs to get quick property loans. Since 2024, the market has professionalized significantly with the rise of Debt Funds, which pool capital from institutional investors to provide "bespoke" lending solutions that move at the speed of the private market. (National Real Estate Investor, 2025)<br>
    <br>4. While private debt provides speed, it carries "maturity and cost" risks. Most private loans have "balloon" maturities; if the borrower cannot sell the property or refinance with a bank before the term ends, they may face heavy extension fees or a "forced sale." Additionally, private lenders often charge "Points" (origination fees) ranging from 1% to 3% of the total loan amount upfront. (RealtyShares, 2026)<br>
    <br>5. To raise capital via private debt, the borrower must provide a detailed "Scope of Work" (SOW) for the property and an "Appraisal" or "Broker Price Opinion" (BPO). The lender will issue a Commitment Letter within 48–72 hours. Closing typically occurs as soon as the title is cleared, often in as little as 7 to 14 days, which is the primary competitive advantage of this capital type. (Geraci Law Firm, 2025)
    </p>
    <p><u><b>References</u></b><br>
    Investopedia. (2026, Jan 04). Hard Money Loan: Definition and How It Works. https://www.investopedia.com/terms/h/hard_money_loan.asp<br>
    Forbes Advisor. (2025, Oct 20). Private Money Lending for Real Estate Investors. https://www.forbes.com/advisor/business-loans/private-money-lending/<br>
    National Real Estate Investor (NREI). (2025). The Rise of Private Debt Funds in CRE. https://www.wealthmanagement.com/real-estate<br>
    RealtyShares. (2026). Bridge Loans vs. Hard Money: What's the Difference? https://www.realtyshares.com/blog/bridge-loans-vs-hard-money<br>
    Geraci Law Firm. (2025, Sept 12). Legal Structures of Private Lending. [suspicious link removed]
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Asset Valuation – The property must have a clear value supported by a third-party appraisal or BPO.<br>
    · Lien Priority – The private lender almost always requires a "First Trust Deed" (first-priority lien).<br>
    · Clear Title – Title insurance is mandatory to ensure no other legal claims exist on the property.<br>
    · Business Purpose Only – Most private lenders will not lend on "owner-occupied" primary residences to avoid consumer protection regulations.<br>
    · LTV Limits – Typically restricted to 65%–75% of the current or improved value.<br>
    · Corporate Ownership – The borrower is often required to be an entity (LLC or Corp) rather than an individual.<br>
    · Hazard Insurance – Builder's Risk or standard hazard insurance must be in place naming the lender as the "loss payee."
    </p>
    <p><b><u>Supporting Document List</u></b><br>
    · Purchase Contract – For new acquisitions.<br>
    · Appraisal Report – Current market value and "As-Completed" value.<br>
    · Scope of Work (SOW) – Detailed line-item budget for any planned renovations.<br>
    · Title Commitment – Showing a clean chain of title.<br>
    · Entity Documents – Articles of Organization and Operating Agreement for the LLC.<br>
    · Photos of the Property – Interior and exterior evidence of current condition.<br>
    · Personal Financial Statement (PFS) – To show the borrower has enough "liquidity" to pay interest and insurance.<br>
    · Exit Strategy Statement – A written plan on how the loan will be repaid (e.g., "Refinance with Bank of America in 12 months").
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request, 'detail.html', context)

def privatedebtrealestateloanfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Debt<br>
    Real Estate Loan</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is a private debt real estate loan?</u></b><br>
    •Answer: A private debt real estate loan is financing provided by private lenders or investors to fund the purchase, development, or refinancing of real estate, often outside traditional banking institutions.
    </p>
    <p><u><b>2. Who typically uses private real estate loans?</u></b><br>
    •Answer: Real estate investors, developers, and businesses that need fast or flexible financing or do not meet traditional bank lending requirements commonly use private real estate loans.
    </p>
    <p><u><b>3. What types of properties can be financed with private real estate loans?</u></b><br>
    •Answer: These loans can finance residential, commercial, industrial, mixed-use, and land development properties.
    </p>
    <p><u><b>4. How much funding can be obtained through private real estate loans?</u></b><br>
    •Answer: Loan amounts vary widely but are generally based on property value, project risk, and borrower experience, ranging from tens of thousands to several million dollars.
    </p>
    <p><u><b>5. How quickly can funds be accessed through private real estate loans?</u></b><br>
    •Answer: Funding can often be accessed much faster than bank loans, sometimes within days or weeks after due diligence and agreement.
    </p>
    <p><u><b>6. How are interest rates structured for private real estate loans?</u></b><br>
    •Answer: Interest rates are typically higher than bank loans and may be fixed or variable, reflecting increased risk and flexible underwriting.
    </p>
    <p><u><b>7. Is collateral required for private real estate loans?</u></b><br>
    •Answer: Yes, the real estate property itself is usually the primary collateral, and lenders may also require personal guarantees.
    </p>
    <p><u><b>8. What repayment terms are common in private real estate loans?</u></b><br>
    •Answer: Terms are often short- to medium-term, ranging from 6 months to 5 years, with options such as interest-only payments or balloon payments.
    </p>
    <p><u><b>9. Do private real estate loans require equity dilution?</u></b><br>
    •Answer: No, private real estate loans are debt instruments and do not require giving up ownership or equity in the business or property.
    </p>
    <p><u><b>10. What are the main advantages of private real estate loans?</u></b><br>
    •Answer: Advantages include fast funding, flexible terms, fewer regulatory requirements, and suitability for non-traditional or complex projects.
    </p>
    <p><u><b>11. What risks are associated with private real estate loans?</u></b><br>
    •Answer: Risks include higher interest costs, shorter repayment terms, refinancing risk, and potential loss of property if repayment obligations are not met.
    </p>
    <p><u><b>12. Can private real estate loans be combined with other financing sources?</u></b><br>
    •Answer: Yes, they are often combined with equity investments, bank financing, mezzanine debt, or construction loans.
    </p>
    <p><u><b>13. How do private real estate loans differ from commercial bank real estate loans?</u></b><br>
    •Answer: Private loans offer faster approval and flexibility but usually have higher costs and shorter terms compared to traditional bank real estate financing.
    </p>
    <p><u><b>14. Are private real estate loans suitable for startups or first-time investors?</u></b><br>
    •Answer: Yes, they can be suitable if the borrower has strong collateral or project potential, though terms may be more conservative.
    </p>
    <p><u><b>15. How can borrowers improve approval chances for private real estate loans?</u></b><br>
    •Answer: Borrowers can improve approval chances by presenting a clear project plan, strong property valuation, exit strategy, and demonstrating experience or professional support.
    </p>
    """)
    context = {
        'introduction':introduction,
    }
    return render(request, 'detail.html', context)

def privatedebtrealestateloantwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Debt</b></u><br>
    Capital Type: Real Estate Loan</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    Private real estate loans are best suited for operating to mature-stage businesses or investors that own or are acquiring real estate. These loans are commonly used for property acquisition, development, renovation, or refinancing, especially when speed or flexibility is required over traditional bank financing. Your stage: {stage}
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Eligible entities include LLCs, C-Corporations, S-Corporations, partnerships, and real estate holding companies. Private lenders often prefer single-purpose entities (SPEs) created specifically to hold the real estate asset. Your entity: {entity}
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Private lenders focus heavily on property value, borrower equity, and exit strategy rather than long operating history. Credit scores and financials are reviewed but are typically less restrictive than banks, provided sufficient collateral exists. Your prior capital: {preraise}
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    This financing operates in the private lending market, outside traditional banking systems. Terms are negotiated directly with private lenders, funds, or high-net-worth individuals, offering greater flexibility but less regulatory protection. Your market type: {premarket}
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    Loan amounts are determined by loan-to-value (LTV) ratios, usually ranging from 50% to 75% of the property's appraised value. Capital raised can range from hundreds of thousands to tens of millions, depending on asset size. Your goal: {raisegoal}
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    Private real estate loans are non-dilutive debt instruments and do not involve equity rounds. They are commonly used as bridge loans, construction loans, or short-term financing prior to refinancing or sale. Your round: {tranch}
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Funding may be provided as a single lump sum for acquisitions or in multiple draws for construction and development projects, based on progress milestones and inspections. Your tranches: {rounds}
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Funds are typically used for property acquisition, construction, renovations, refinancing, or bridge financing. Personal use or unrelated business expenses are strictly prohibited. Your use: {useoffund}
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Borrower risk is high, as default may result in foreclosure or forced asset sale. Lender risk is mitigated by real estate collateral but can increase during market downturns or valuation declines.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Interest rates are higher than bank real estate loans but lower than unsecured private debt. Rates reflect shorter terms, higher flexibility, and faster execution, often accompanied by points or exit fees. Your cost: {enterprisecost}
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs commonly include origination fees, appraisal costs, legal fees, inspection fees, and lender points, which are generally higher than traditional commercial bank loans. Your upfront cost: {upfrontcost}
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    Timing to capital is fast, typically 2–6 weeks, making private real estate loans ideal for time-sensitive transactions or deals that cannot wait for bank approval. Your timeline: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction': introduction,
    }
    return render(request, 'detail.html', context)