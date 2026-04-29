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

def hedgefundspublic(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Hedge Funds</b></u><br>
    Capital Type: Public </center></p>
    <p><b><u>Introduction</u></b><br>
Public Hedge Funds are ideal for sophisticated investors seeking actively managed, market-exposed investment vehicles that pursue absolute or risk-adjusted returns through trading strategies in publicly listed securities. They are designed so that pooled capital is deployed across equities, fixed income, derivatives, and other liquid instruments using long, short, and arbitrage strategies to capitalize on market inefficiencies. {n} fits that definition. In 2026, public hedge funds remain a prominent component of global capital markets, particularly in equity long/short, global macro, event-driven, and relative-value strategies. While access is often limited to accredited or qualified investors, these funds operate primarily in public markets and offer higher liquidity relative to private investment funds. While public hedge funds provide diversification and potential downside protection, they introduce market, leverage, and manager risk. Performance depends heavily on manager skill, risk controls, and market conditions.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Public Hedge Fund is an alternative investment fund that primarily trades publicly listed securities and derivatives, employing active management strategies such as long/short equity, global macro, arbitrage, and event-driven investing to generate absolute or risk-adjusted returns. (Securities and Exchange Commission, 2025)
<br>


    <br>2.  Public hedge funds sit outside the traditional Capital Stack, as they represent pooled investment vehicles rather than financing instruments. Investors acquire fund interests rather than direct claims on underlying portfolio assets or operating companies. (Financial Stability Board, 2025)
<br>

    <br>3. Legally, public hedge funds are structured as limited partnerships or limited liability companies and governed by a Private Placement Memorandum (PPM) and fund operating agreement. They are subject to securities regulations governing investment advisers, disclosures, and trading practices. (U.S. Securities and Exchange Commission, 2025)
<br>
    <br>4.From a risk perspective, public hedge funds expose investors to market volatility, leverage, liquidity, and counterparty risk. The use of derivatives and short selling can amplify gains and losses, making robust risk management and transparency critical. (Bank for International Settlements, 2025)
<br>
    <br>5.
From an accounting and process standpoint, public hedge funds report investor capital as Net Asset Value (NAV), with periodic subscriptions and redemptions subject to notice periods and lock-ups. Performance fees and management fees are calculated based on fund NAV and realized gains. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>U.S. Securities and Exchange Commission (SEC). (2025). Hedge Fund Regulation and Disclosure. <a href="https://www.sec.gov/hedge-funds">https://www.sec.gov/hedge-funds</a>
<br>
    <br>Financial Stability Board (FSB). (2025). Global Hedge Fund Market Overview. <a href="https://www.fsb.org">https://www.fsb.org</a>
<br>
    <br>Bank for International Settlements (BIS). (2025). Market Risk and Leverage in Hedge Funds. <a href="https://www.bis.org">https://www.bis.org</a>
<br>
    <br>Deloitte. (2025). Accounting and Valuation for Hedge Funds. <a href="https://www2.deloitte.com/hedge-funds">https://www2.deloitte.com/hedge-funds</a>
<br>
    <br>CFA Institute. (2025). Hedge Fund Strategies and Risk Management. <a href="https://www.cfainstitute.org">https://www.cfainstitute.org</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Investor Eligibility - Accredited or qualified investor status
<br>•   Fund Registration - Investment adviser and regulatory filings
<br>•   Disclosure Requirements - PPM and ongoing investor reporting
<br>•   Trading & Market Conduct Rules - Compliance with securities laws
<br>•   Leverage Limits - Risk and exposure management policies
<br>•   Valuation Policies - NAV calculation and independent oversight
<br>•   Anti-Money Laundering (AML) - KYC and compliance checks
<br>•   Redemption Terms - Liquidity, lock-ups, and notice periods


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Private Placement Memorandum (PPM) - Fund strategy and risk disclosures
<br>•   Limited Partnership or Operating Agreement - Governance terms
<br>•   Subscription Agreement - Investor onboarding documentation
<br>•   Investor Eligibility Certifications - Accredited investor verification
<br>•   Valuation Policy - NAV calculation methodology
<br>•   Risk Management Policy - Leverage and exposure controls
<br>•   Compliance Manual - Regulatory adherence procedures
<br>•   Audited Financial Statements - Independent fund audits

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def hedgefundspublicfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Hedge Funds<br>
    Public</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are public hedge funds?</u></b><br>
    •Answer: Public hedge funds are hedge fund investment vehicles that offer access to hedge fund strategies through publicly available or regulated structures.
</p>

    <p><u><b>2. How do public hedge funds differ from traditional hedge funds?</u></b><br>
    •Answer: Public hedge funds offer greater transparency, regulatory oversight, and lower minimum investment requirements compared to private hedge funds.
</p>

    <p><u><b>3. Who can invest in public hedge funds?</u></b><br>
    •Answer: Depending on jurisdiction, public hedge funds may be available to retail or semi-professional investors, not just accredited investors.
</p>

    <p><u><b>4. What strategies do public hedge funds use?</u></b><br>
    •Answer: Strategies may include long/short equity, global macro, event-driven, arbitrage, and market-neutral approaches.
</p>

    <p><u><b>5. How do public hedge funds work?</u></b><br>
    •Answer: Investors buy units or shares in a regulated fund that employs hedge fund strategies to generate returns.
</p>

    <p><u><b>6. Are public hedge funds regulated?</u></b><br>
    •Answer: Yes, they are subject to regulatory oversight, disclosure requirements, and investor protection rules.
</p>

    <p><u><b>7. What are the typical liquidity terms of public hedge funds?</u></b><br>
    •Answer: Liquidity is generally higher than private hedge funds, with daily, weekly, or monthly redemption options.
</p>

    <p><u><b>8. What fees are charged by public hedge funds?</u></b><br>
    •Answer: Fees typically include a management fee and sometimes a performance fee, though often lower than traditional hedge funds.
</p>

    <p><u><b>9. What are the risks of public hedge funds?</u></b><br>
    •Answer: Risks include market risk, strategy risk, leverage risk, and underperformance during certain market conditions.
</p>

    <p><u><b>10. Do public hedge funds use leverage?</u></b><br>
    •Answer: Yes, many public hedge funds use leverage, though within regulated limits.
</p>

    <p><u><b>11. How are public hedge funds valued?</u></b><br>
    •Answer: Fund assets are typically valued regularly using market prices and standardized valuation methods.
</p>

    <p><u><b>12. What are the benefits of investing in public hedge funds?</u></b><br>
    •Answer: Benefits include diversification, access to hedge fund strategies, and improved liquidity and transparency.
</p>

    <p><u><b>13. How do public hedge funds differ from mutual funds?</u></b><br>
    •Answer: Public hedge funds have more flexible investment strategies and may use leverage and short-selling, unlike traditional mutual funds.
</p>

    <p><u><b>14. Are public hedge funds suitable for all investors?</u></b><br>
    •Answer: No, they are best suited for investors with higher risk tolerance and understanding of alternative strategies.
</p>

    <p><u><b>15. When should investors consider public hedge funds?</u></b><br>
    •Answer: Investors should consider public hedge funds when seeking diversified returns, alternative strategies, and regulated hedge fund exposure.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def hedgefundspublictwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Hedge Funds</b></u><br>
    Capital Type: Public</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Public hedge fund capital is best suited for mature companies with established operations, public market visibility, and sufficient scale to meet the investment and liquidity requirements of hedge fund strategies. This capital is inappropriate for early-stage startups.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Target companies are generally publicly listed C-Corporations or entities structured to access public markets. Private entities may engage indirectly if preparing for public listing, but sole proprietorships are not suitable.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Companies engaging with public hedge funds usually have significant prior capitalization, public equity float, and existing institutional investor participation. Investment decisions are driven by market dynamics, liquidity, valuation, and trading opportunities.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Public hedge funds operate within the global public capital markets and deploy capital across listed equities, bonds, derivatives, and structured instruments. These markets emphasize liquidity, transparency, and pricing efficiency.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Capital deployed by public hedge funds can range from tens of millions to billions of dollars, depending on fund size, strategy, and conviction. The amount depends on market liquidity, trading volume, and position sizing rather than predefined raise targets.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Hedge fund investments in public markets do not constitute capital rounds in the traditional sense. Capital is typically deployed through open-market purchases, private investment in public equity transactions, or structured trades.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Capital deployment often occurs incrementally through multiple trades over time rather than a single tranche. Position sizes may be built, adjusted, or exited dynamically based on market conditions and investment performance.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Funds raised through public-market transactions are generally used for:
<br>•   General corporate purposes and growth initiatives
<br>•   Balance sheet optimization and debt repayment
<br>•   Acquisitions and strategic investments
Use of funds is typically unrestricted unless tied to a specific structured transaction.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to hedge funds includes market volatility, liquidity risk, regulatory changes, and company-specific performance risk. For companies, risk includes stock price volatility, activist pressure, and increased market scrutiny associated with hedge fund involvement.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is reflected in market pricing, dilution from equity issuance if applicable, and potential volatility rather than explicit interest or fees.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs for companies are generally low when hedge fund capital is accessed through open-market trading. Costs may increase in structured transactions such as PIPEs due to legal, advisory, and compliance expenses.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital in public hedge fund engagement is market-driven and can be immediate through open-market transactions or take several weeks in structured deals. Access is highly dependent on market conditions, liquidity, and investor sentiment.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
