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


def bonds(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Bonds</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Bonds are an ideal financing tool for companies looking to raise capital in amounts ranging from a few million to several billion dollars, depending on the company’s financial status and the bond’s structure. They offer a way for companies to borrow money from investors and repay them with interest over a set period. {n} fits that definition. Bonds have been a widely used financing method for decades and continue to be a staple for raising significant capital. For example, in 2024, the global bond market saw over $1.5 trillion in corporate bond issuance. In 2023, corporate bonds issued in the U.S. alone raised over $500 billion, with investment-grade bonds accounting for the majority. The average size of each corporate bond issuance in 2023 was $300 million, with large issuances from major corporations driving the market's overall valuation. There are several types of bonds available, including corporate bonds, municipal bonds, and government bonds, each varying in risk, return, and terms depending on the issuer. However, bonds come with risks, including interest rate risk, credit risk, and liquidity risk, all of which can impact the company's ability to repay or the bondholder’s return on investment. There are five types of bonds you can match with: 1) Foreign Bonds, 2) Mortgage Backed Bonds, 3) Government Backed Bonds, 4) High Yield Junk Bonds, 5) Investment Grade Bonds. We will match you with the best bonds type for your business as per your business needs.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. A bond is a form of debt financing where a company or government borrows money from investors in exchange for regular interest payments, typically called coupon payments, and a promise to repay the principal (the amount borrowed) at the bond's maturity. For a company that qualifies for bonds, this means issuing bonds to raise capital for various business needs such as expansion, acquisitions, or debt refinancing. Investors who purchase the bonds are essentially lending money to the company, and in return, they receive periodic interest payments until the bond matures, at which point the company repays the principal. To qualify for issuing bonds, a company typically needs a solid financial track record, stable revenue streams, and the ability to meet repayment obligations, making it an ideal option for established businesses looking to raise large amounts of capital without giving up ownership or equity. (SEC, n.d.)
<br>
    <br>2. There are several different types of bonds that companies and governments can issue to raise capital, each with distinct characteristics. Corporate bonds are issued by companies and typically offer higher interest rates to compensate for the risk of investing in a private entity. Government bonds, such as Treasury bonds in the U.S., are issued by the federal government and are considered low-risk because they are backed by the government's credit. Municipal bonds are issued by local governments or municipalities to fund projects like infrastructure, and their interest may be exempt from federal taxes. Convertible bonds allow bondholders to convert their debt into a predetermined amount of the company's equity, which can be appealing if the company’s stock price appreciates. Zero-coupon bonds do not pay periodic interest; instead, they are issued at a discount and the full-face value is paid at maturity. Each type of bond carries its own risk and return profile, making it important for investors and issuers to carefully consider which bond type best meets their financing or investment needs. (Jark. 2025)
<br>
    <br>3. Bonds have a long and storied history, with their origins tracing back to ancient civilizations. The first known use of bonds as a form of debt issuance occurred in ancient Mesopotamia, where clay tablets were used to record transactions involving borrowing and lending, much like modern bonds. However, the concept of bonds as we know them today began to take shape in the 17th century, with the issuance of government bonds in Europe, particularly by the Dutch and English governments to finance wars and infrastructure projects. The British government issued the first national bond in 1693 to fund the war with France, marking the beginning of modern bond markets. Over the centuries, bonds have evolved from government debt instruments to include corporate bonds, municipal bonds, and various other forms, becoming a critical component of financial markets. Today, bonds are used by governments, municipalities, and corporations worldwide as a means of raising capital, with the global bond market being one of the largest and most diverse financial markets in existence. (Written by: Arianne Bonacua, n.d.)
<br>
    <br>4. Bonds, while often considered safer investments compared to stocks, still carry a variety of risks that companies and investors must carefully consider. The primary risk is credit risk, which refers to the possibility that the bond issuer might default on its debt obligations, leading to financial losses for bondholders. Another significant risk is interest rate risk, where changes in market interest rates can cause bond prices to fluctuate; if interest rates rise, the value of existing bonds typically decreases. Additionally, inflation risk can erode the purchasing power of bond returns, especially for long-term bonds with fixed interest payments. Liquidity risk is another concern, particularly for bonds that are not actively traded, making it difficult to sell the bonds without incurring a loss. Finally, call risk can arise when issuers redeem bonds before their maturity date, often in declining interest rate environments, limiting the bondholder’s returns. Understanding and managing these risks are essential for companies and investors when using bonds as a financing tool. (Edge, 2023)
<br>
    <br>5. To use bonds as a capital type, a company must meet several key requirements. First, the company needs to have a solid financial history, demonstrating stable revenue streams, profitability, and a strong balance sheet to reassure investors that it can repay the bond’s principal and interest. The company should also have a clear plan for how the raised funds will be utilized, typically for expansion, acquisitions, or other capital-intensive projects. Legal and regulatory compliance is critical, meaning the company must adhere to securities laws and may need to file with regulatory bodies such as the Securities and Exchange Commission (SEC) if issuing bonds to the public. Furthermore, companies must have a favorable credit rating, as this will affect the bond's interest rate and marketability. Bond issuance also requires proper governance and the ability to manage the debt, ensuring that the company can make timely interest payments and eventually repay the principal upon maturity. Lastly, the company must be able to present credible financial forecasts and projections to attract potential bondholders. (Bonds, Investor.gov (n.d.)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>SEC’s Office of Investor Education and Advocacy. (n.d.). Investor Bulletin: What are corporate bonds? Investor Bulletin. <a href="https://www.sec.gov/files/ib_corporatebonds.pdf">https://www.sec.gov/files/ib_corporatebonds.pdf</a>
    <br><br>Jark, D. (2025, January 28). Types of bonds and how they work. Investopedia. <a href="https://www.investopedia.com/financial-edge/0312/the-basics-of-bonds.aspx">https://www.investopedia.com/financial-edge/0312/the-basics-of-bonds.aspx</a>
    <br><br>Written by: Arianne Bonacua. (n.d.). A Timeline history of bonds | Markets.com. A Timeline History of Bonds | markets.com. <a href="https://www.markets.com/education-centre/history-of-bonds/">https://www.markets.com/education-centre/history-of-bonds/</a>
    <br><br>Edge, M. (2023, May 25). Understanding Bonds: The risks & Types of bond investments. Merrill Edge. <a href="https://www.merrilledge.com/article/understanding-bonds-and-their-risks?">https://www.merrilledge.com/article/understanding-bonds-and-their-risks?</a>
    <br><br>Bonds | Investor.gov. (n.d.). <a href="https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds">https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds</a>
    </p>
    <p><b><u>Qualification Requirements</u></b>
    <br>• Legal Structure: The company must be a legal entity, typically a corporation or LLC.
    <br>• Regulatory Registration: The company must register the bond offering with relevant securities regulators, like the SEC (unless exempt).
    <br>• Credit Rating: A credit rating from an agency is often required to assess the company’s ability to repay the debt.
    <br>• Covenants and Terms: The company must agree to bond covenants, which include repayment terms and financial restrictions.
    <br>• Legal Documents: The company must prepare and file necessary documents like the bond indenture and offering prospectus.
    <br>• Compliance with Securities Laws: The company must adhere to securities laws, ensuring transparency with investors.
    <br>• Debt Issuance Approval: The board and potentially shareholders must approve the bond issuance.
    <br>• Debt-to-Equity Ratio: The company must manage its debt-to-equity ratio to avoid overleveraging.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Prospectus/Offering Memorandum – Outlines the bond terms, risks, and purpose.
    <br>• Bond Indenture – The legal agreement with bondholders detailing bond terms.
    <br>• Registration Statement (SEC Filings) – Required for public offerings to ensure compliance with regulations.
    <br>• Financial Statements – Audited financials to demonstrate the company’s financial health.
    <br>• Credit Rating Report – An assessment of the company’s creditworthiness.
    <br>• Board Resolutions – Proof that the board authorized the bond issuance.
    <br>• Legal Opinions – Confirmations of legal compliance for the bond issuance.
    <br>• Use of Proceeds Statement – Explains how funds from the bond sale will be used.
    <br>• Debt Agreements and Covenants – Details on existing debts and related covenants to avoid conflicts.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def bondsfaq(request):
    introduction = mark_safe("""
                      
    <p><b><u>FAQs</u></b></p>
    <p><b><u>1. What is a bond?</u></b><br>
    • Answer: A bond is a debt security in which an investor loans money to an entity (such as a corporation, government, or municipality) in exchange for periodic interest payments and the return of the principal amount at the maturity date.
    </p>
                             
    <p><b><u>2. Who can issue bonds?</u></b><br>
    • Answer: Bonds can be issued by various entities, including governments (local, state, and federal), corporations, municipalities, and other organizations. Corporations typically issue bonds to raise capital for projects or to refinance debt.
    </p>
                             
    <p><b><u>3. What are the different types of bonds?</u></b><br>
    • Answer: The main types of bonds include:
    <br>• Corporate Bonds: Issued by corporations to raise capital.
    <br>• Municipal Bonds: Issued by local governments or states.
    <br>• Treasury Bonds: Issued by the federal government to fund operations.
    <br>• Convertible Bonds: Bonds that can be converted into a predetermined number of shares of the issuer’s stock.
    <br>• High-Yield Bonds: Issued by companies with lower credit ratings, offering higher interest rates due to the increased risk.
    </p>
                             
    <p><b><u>4. How do bonds work?</u></b><br>
    • Answer: When you buy a bond, you're lending money to the issuer for a set period. The issuer agrees to pay you interest at regular intervals, and at the end of the term (maturity), the issuer repays the principal amount of the bond.</p>
                             
    <p><b><u>5. What is the bond's interest rate?</u></b><br>
    • Answer: The bond’s interest rate, also known as the coupon rate, is the annual interest paid by the issuer, usually expressed as a percentage of the face value of the bond.
    </p>
                             
    <p><b><u>6. What is a bond’s face value?</u></b><br>
    • Answer: The face value (or par value) is the amount that will be paid back to the bondholder at maturity. Typically, bonds have a face value of $1,000.</p>
                             
    <p><b><u>7. What is a bond rating?</u></b><br>
    • Answer: A bond rating is an evaluation of the creditworthiness of the issuer and the likelihood that the issuer will be able to meet its debt obligations. Agencies like Standard & Poor's, Moody's, and Fitch provide these ratings. Higher ratings indicate lower risk, while lower ratings indicate higher risk.</p>
                             
    <p><b><u>8. What is the maturity date of a bond?</u></b><br>
    • Answer: The maturity date is the date when the bond's principal amount is due to be repaid by the issuer. Bonds can have short-term (1-5 years), medium-term (5-10 years), or long-term (over 10 years) maturities.</p>
                             
    <p><b><u>9. What is the yield of a bond?</u></b><br>
    • Answer: The yield is the return an investor can expect to earn if the bond is held to maturity. It considers both the interest payments (coupon payments) and any capital gains or losses due to price fluctuations.</p>
                             
    <p><b><u>10. What are the risks associated with bonds?</u></b><br>
    • Answer: The main risks involved in bond investing include:
    <br>• Interest Rate Risk: The value of bonds decreases as interest rates rise.
    <br>• Credit Risk: The issuer may default on its obligations to pay interest or repay principal.
    <br>• Inflation Risk: Inflation may erode the purchasing power of the bond's future cash flows.
    <br>• Liquidity Risk: Some bonds may be difficult to sell before maturity without incurring significant losses.
    </p>
                             
    <p><b><u>11. How are bonds taxed?</u></b><br>
    • Answer: The tax treatment of bond interest depends on the type of bond and the investor's jurisdiction. Interest on U.S. Treasury bonds is exempt from state and local taxes, while corporate and municipal bond interest may be subject to federal, state, or local taxes.</p>
                             
    <p><b><u>12. Why do companies issue bonds instead of stocks?</u></b><br>
    • Answer: Companies issue bonds to raise capital without giving up ownership or control of the company. Bonds allow companies to access capital while avoiding dilution of their equity base.
    </p> 
                             
    <p><b><u>13. How do I buy bonds?</u></b><br>
    • Answer: Bonds can be purchased through brokers, financial advisors, or directly from the government (in the case of government bonds). Bond investors can choose from new bond issuances or buy bonds on the secondary market.</p>

    <p><b><u>14. What happens if a company defaults on a bond?</u></b><br>
    • Answer:If a company defaults on its bond, it may fail to make interest payments or repay the principal. Bondholders may be able to claim the company’s assets in a bankruptcy proceeding, though bondholders typically take a loss if the company is insolvent.</p>        
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def bondstwelve(request):
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
    premarketStr = ''

    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' : 'it cannot pursue a bond offering with legal support and debt advisory as the cost to raise capital through bonds is higher.',
        'Minimum $500 - Maximum $999' :  'it cannot pursue a bond offering with legal support and debt advisory as the cost to raise capital through bonds is higher.',
        'Minimum $1000 - Maximum $2499' :  'it cannot pursue a bond offering with legal support and debt advisory as the cost to raise capital through bonds is higher.',
        'Minimum $2500 - Maximum $4999' :  'it cannot pursue a bond offering with legal support and debt advisory as the cost to raise capital through bonds is higher.',
        'Minimum $5000 - Maximum $9999' :  'it cannot pursue a bond offering with legal support and debt advisory as the cost to raise capital through bonds is higher.',
        'Minimum $10000 - Maximum $24999' : 'it cannot pursue a bond offering with legal support and debt advisory as the cost to raise capital through bonds is higher.',
        'Minimum $25000 - Maximum $49999' : 'it cannot pursue a bond offering with legal support and debt advisory as the cost to raise capital through bonds is higher.',
        'More than $50000+' : 'it can pursue a bond offering with legal support and debt advisory.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'does not match the time required to raise capital by issuing bonds.',
        '1 Week to 2 Week' : 'does not match the time required to raise capital by issuing bonds.',
        '2 Weeks to 4 Weeks' : 'does not match the time required to raise capital by issuing bonds.',
        '1 Month to 2 Months' : 'does not match the time required to raise capital by issuing bonds.',
        '2 Months to 3 Months' : 'does not match the time required to raise capital by issuing bonds.',
        '3 Months to 6 Months' : 'matches the time required to raise capital by issuing bonds.',
        '6 Months to 12 Months' : 'matches the time required to raise capital by issuing bonds.',
        'More than 1 year' : 'matches the time required to raise capital by issuing bonds.',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()

    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Bonds</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    Bond financing is typically suitable for later-stage or revenue-generating companies that can demonstrate predictable cash flow and strong creditworthiness. Unlike equity or VC rounds, bonds do not dilute ownership and provide fixed-income investors with security over interest and principal repayment.
    <br><br>If {n} is in a {stage} stage with stable revenue streams, issuing debt via bonds can offer non-dilutive capital to fund infrastructure, M&A, or large capital expenditures without giving up equity.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Bond issuance requires {n} to be a formally registered legal entity, typically a C Corporation or LLC with established financial reporting and governance practices.
    Institutional or public bond offerings also require:
    • Audited financial statements
    • Corporate governance structures
    • Legal disclosures compliant with SEC or relevant regulatory standards
    If {n} is planning a private placement, it can issue bonds to accredited investors or institutions without SEC registration, provided it meets private offering exemptions (e.g., Reg D).
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    If {n} has already raised {preraise} through pre-capital (from equity, grants, or revenue), this reduces default risk and makes the company more attractive to bondholders. Pre-capital also demonstrates operational maturity—bond investors want assurance that {n} can service debt through existing or projected income.
    <br><br>{n}’s pre-capital track record will be critical when negotiating interest rates, covenants, and collateral terms.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    If {n}’s prior capital came from {premarketstr}, adding bonds diversifies its capital structure and reduces dilution.
    <br><br>• Prior equity raises improve balance sheet strength
    <br>• Revenue-based or grant capital lowers perceived default risk
    <br>• Introducing convertible bonds or revenue-backed bonds can bridge investor interest between debt and equity
    <br><br>Bond strategies are most powerful when {n} is ineligible or uninterested in further equity dilution but still needs mid-to-large-scale funding.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If {n} plans to raise {raisegoal} in the next 12–18 months, bond issuance can be structured as:
    • Senior secured bonds (lower interest, collateralized)
    • Unsecured notes (higher interest, no collateral)
    • Revenue-based financing (variable payments tied to income)
    • Convertible bonds (debt that converts to equity under specific conditions)
    {n} must present a solid repayment plan, debt service coverage ratio (DSCR), and realistic growth forecast to access these options.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Bond financing doesn’t follow the traditional Series A/B/C model. Instead, {n} can raise in tranches, depending on:
    <br><br>• Revenue milestones
    <br>• Capital expenditure phases
    <br>• Asset acquisitions or infrastructure needs
    <br><br>This approach is ideal if {n} wants to finance specific projects or fund operations in parallel to equity rounds without affecting cap table ownership.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Bond capital is often released in phases, tied to:
    <br><br>• Project completion or operational milestones
    <br>• Collateral value updates
    <br>• Ongoing financial health (e.g., EBITDA or cash flow targets)
    <br>For example, {n} could raise an initial $2M bond with a first $1M released upfront, and the next $1M contingent on reaching $100K in monthly revenue or completing a pilot expansion.
    <br><br>Bond investors often require reporting frequency (monthly/quarterly) and covenants that protect their position.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    <br>Bond proceeds are best deployed into predictable, high-yield, or infrastructure-heavy initiatives, such as:
    <br><br>• Capital expenditures (equipment, real estate, vehicles)
    <br>• R&D investment for IP-heavy firms
    <br>• Expansion into new markets or geographies
    <br>• Bridge financing for acquisitions or IPO prep
    <br>• Refinancing higher-interest or short-term debt
    <br><br>{n} should allocate these funds toward clear, revenue-generating growth, and avoid deploying bond capital into speculative or untested product development.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Bond strategies carry lower investor risk than equity (due to interest payments and priority in liquidation) but can impose higher financial risk on the company, including:
    <br><br>• Fixed repayment obligations
    <br>• Default penalties
    <br>• Financial covenants and credit reviews
<br>
    <br>To mitigate these risks, {n} should:
    <br>• Maintain strong revenue visibility and forecast accuracy
    <br>• Limit total debt to manageable leverage ratios (e.g., Debt/EBITDA < 3x)
    <br>• Consider credit insurance or securing bonds against assets
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Bond capital cost is interest-based rather than equity-based. While {n} avoids dilution, it must factor in:
    <br><br>• Interest rates (6%–12%) depending on risk profile
    <br>• Issuance costs (~2%–5% of capital raised)
    <br>• Legal and rating agency fees (if applicable)
<br>
    <br>Total cost of capital may be lower than equity—but only if repayment is predictable and {n} maintains healthy margins.
    <br><br>Convertible or revenue-based bonds may carry hybrid costs (e.g., caps on returns, equity triggers), giving {n} more flexibility while managing cash flow.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Bond issuance involves significant upfront legal and advisory expenses, including:
    <br><br>• Legal structuring & term sheet drafting: $10K–$30K
    <br>• Private placement memoranda (PPM): $5K–$20K
    <br>• Third-party valuation or collateral assessment: $5K–$15K
    <br>• Optional: credit rating fees or trustee setup for large issues
<br>
    <br>If {n} has a {upfrontcost} capital formation budget, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Bond financing—especially through private placements or institutional lenders—can close in 12–52 weeks, depending on:
    <br><br>• Deal complexity
    <br>• Collateral evaluation
    <br>• Investor due diligence

    <br><br>{n} can accelerate closing time by preparing:
    <br>• 3 years of financials (actual + projected)
    <br>• Audited statements or GAAP-compliant books
    <br>• Use-of-funds plan with ROI and debt service modeling
    <br>• Legal documentation and disclosure readiness
    <br><br> Your time of {upfronttime} for raising capital {timeanalysis} 
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,costanalysis=costanalysis,premarketstr=premarketStr,timeanalysis=timeanalysis))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)