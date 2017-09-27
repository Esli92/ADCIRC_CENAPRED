conditional_quantile <- function (pred, obs, bins = NULL, thrs = c(10, 20), main = "Conditional Quantile Plot", 
    ...) 
{
    old.par <- par(no.readonly = TRUE)
    on.exit(par(old.par))
    if (!is.null(bins)) {
        if (min(bins) > min(obs) | max(bins) < max(obs)) {
            warning("Observations outside of bin range. \n")
        }
        if (min(bins) > min(pred) | max(bins) < max(pred)) {
            warning("Forecasts outside of bin range. \n")
        }
    }
    else {
        dat <- c(obs, pred)
        min.d <- min(dat)
        max.d <- max(dat)
        bins <- seq(floor(min.d), ceiling(max.d), length = 11)
    }
    lo <- min(bins)
    hi <- max(bins)
    b <- bins[-length(bins)]
    labs <- b + 0.5 * diff(bins)
    obs.cut <- cut(obs, breaks = bins, include.lowest = TRUE, 
        labels = labs)
    obs.cut[is.na(obs.cut)] <- labs[1]
    obs.cut <- as.numeric(as.character(obs.cut))
    frcst.cut <- cut(pred, breaks = bins, include.lowest = TRUE, 
        labels = labs)
    frcst.cut[is.na(frcst.cut)] <- labs[1]
    frcst.cut <- as.numeric(as.character(frcst.cut))
    n <- length(labs)
    lng <- aggregate(obs, by = list(frcst.cut), length)
    med <- aggregate(obs, by = list(frcst.cut), median)
    q1 <- aggregate(obs, by = list(frcst.cut), quantile, 0.25)
    q2 <- aggregate(obs, by = list(frcst.cut), quantile, 0.75)
    q1$x[lng$x <= thrs[1]] <- NA
    q2$x[lng$x <= thrs[1]] <- NA
    q3 <- aggregate(obs, by = list(frcst.cut), quantile, 0.1)
    q4 <- aggregate(obs, by = list(frcst.cut), quantile, 0.9)
    q3$x[lng$x <= thrs[2]] <- NA
    q4$x[lng$x <= thrs[2]] <- NA
    par(mar = c(5, 5, 5, 5))
    plot(frcst.cut, obs.cut, xlim = c(lo, hi), ylim = c(lo, hi), 
        main = main, type = "n", 
        ...)
    mtext("Sample Size", side = 4, adj = -1)
    legend.txt <- c("Mediana", "Cuantiles 25/75", " Percentiles 10/90")
    legend(min(pred) + 0.55 * diff(range(pred)), min(obs) + 0.25 * 
        diff(range(obs)), legend.txt, col = c(2, 3, 4), lty = c(1, 
        2, 3), lwd = 3, cex = 0.7)
    abline(0, 1)
    X <- as.numeric(as.character(med$Group.1))
    lines(X, med$x, col = 2, lwd = 3)
    lines(X, q1$x, col = 3, lty = 2, lwd = 3)
    lines(X, q2$x, col = 3, lty = 2, lwd = 3)
    lines(X, q3$x, col = 4, lty = 3, lwd = 3)
    lines(X, q4$x, col = 4, lty = 3, lwd = 3)
    pp <- par("plt")
    par(plt = c(pp[1], pp[2], pp[3], 0.2))
    par(new = TRUE)
    hist(frcst.cut, breaks = bins, col = "blue", main = "", axes = FALSE, 
        xlim = c(lo, hi), xlab = " ", ylab = " ")
    axis(4, line = 0)
}
